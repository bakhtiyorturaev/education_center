from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path("", profiles, name="profiles"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("account/", account, name="account"),
    path("account_edit/", account_edit, name="account_edit"),
    path("profiles/<str:id>", profile, name="profile"),
    path("account/skills_add/", skills_add, name="skills_add"),
    path('skill/<uuid:skill_id>/edit/', skill_edit, name='skill_edit'),
    path('skill/<uuid:skill_id>/delete/', skill_delete, name='skill_delete'),

]