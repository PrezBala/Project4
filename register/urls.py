from django.urls import path, include
from .views import (
    signup, signin, update_profile, logout)


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("update_profile/", update_profile, name="update_profile"),
    path("logout/", logout, name="logout"),
]
