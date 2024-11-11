from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserSerializer, HabitSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .tasks import *
from .models import User, Habit
from celery.result import AsyncResult

class CreateUserView(generics.CreateAPIView):
    """
    Create a new user with the given credentials.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class HabitListView(generics.ListCreateAPIView):
    """
    List all habits or create a new habit.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """"
        Return a list of habits for the authenticated user.
        """
        user = self.request.user
        return Habit.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Create a new habit for the current authenticated user.
        """
        user_id = self.request.user.id
        habit_data = serializer.validated_data

        create_habit.delay(user_id, habit_data)


class HabitDeleteView(generics.DestroyAPIView):
    """
    Delete habits for the authenticated user.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """
        Delete habit with the given ID for the authenticated user.
        """
        habit_id = self.kwargs['pk']
        task = delete_habit.delay(habit_id)

        task_result = AsyncResult(task.id)

        try:
            task_result.successful()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise Exception(f"Could not delete habit: {e}")


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Receive access token after logging in.
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]