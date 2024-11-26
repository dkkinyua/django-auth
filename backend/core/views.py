from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.serializers import UserSerializer

# Create your views here.

# Test view
@api_view(["GET"])
def index(request):
    return render(request, 'core/index.html')

# Create a new user
@api_view(["POST"])
def register(request):
    data = request.data

    if not data:
        return Response({"detail": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
    
    new_user = User.objects.create(
        username = data["username"],
        email = data["email"],
        password = make_password(data["password"]),
        is_active = False
    )

    serializer = UserSerializer(new_user, many=False)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

