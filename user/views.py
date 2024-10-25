from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, HabitSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Habit

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
        serializer.save(user=self.request.user)


class HabitDeleteView(generics.DestroyAPIView):
    """
    Delete habits for the authenticated user.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of habits for the authenticated user.
        """
        user = self.request.user
        return Habit.objects.filter(user=user)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Receive access token after logging in.
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]