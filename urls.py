from django.urls import path, include
from account import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("users/", views.user_list, name="user_list"),
    path("users/<username>", views.user_detail, name="user_detail"),
]
