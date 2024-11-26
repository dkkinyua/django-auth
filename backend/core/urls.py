from django.urls import path
from core import views

urlpatterns = [
    path("index/", views.index, name='test-url'),
    path("auth/users/", views.register, name='register-users'),
]