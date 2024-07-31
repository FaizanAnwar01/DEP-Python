# myapp/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .serializers import UserSerializer  # Import UserSerializer here
from django.contrib.auth.models import User

def home(request):
    return HttpResponse("<h1>Welcome to My Django App. It's my 1st time with development in python using command lines.</h1>")

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def home(request):
        return HttpResponse("<h1>Welcome to My Django App</h1>")

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Success"})
        else:
            return Response({"detail": "Invalid credentials"}, status=400)
        
