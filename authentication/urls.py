from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegistrationView, CustomLoginView

"""
URL configuration for user-related API endpoints.

This module defines URL patterns for user profiles, registration, and login.

Endpoints:
- /profiles/ : List or create user profiles (UserProfileList)
- /profiles/<int:pk>/ : Retrieve, update, or delete a specific user profile (UserProfileDetail)
- /register/ : Register a new user (RegistrationView)
- /login/ : User login with email and password (CustomLoginView)
"""

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login')
]
