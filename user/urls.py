from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("habits/", views.HabitListView.as_view(), name="habit-list"),
    path("habits/delete/<int:pk>/", views.HabitDeleteView.as_view(), name="delete-habit"),
]