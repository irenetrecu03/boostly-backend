from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("auth/", include("rest_framework.urls")),
    path("user/", include("user.urls")),
]
