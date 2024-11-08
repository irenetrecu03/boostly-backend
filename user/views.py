from rest_framework import generics, status
from .serializers import UserSerializer, HabitSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .tasks import create_habit, delete_habit, get_habit_list
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
        user_id = self.request.user.id
        habits = get_habit_list(user_id)
        return habits

    def perform_create(self, serializer):
        """
        Create a new habit for the current authenticated user.
        """
        user_id = self.request.user.id
        habit_data = serializer.validated_data

        task = create_habit.delay(user_id, habit_data)
        result = AsyncResult(task.id)
        print(task.id, result.status)


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
        habit_id = self.kwargs['id']
        delete_habit.delay(habit_id)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Receive access token after logging in.
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]