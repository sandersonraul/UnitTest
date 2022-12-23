from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages, auth
import json

class RegistrationView(View):
  def get(self, request):
    return render(request, "register.html")

  def post(self, request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]

    if not User.objects.filter(username=username).exists():
      if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect(reverse('login'))

class LoginView(View):
  def get(self, request):
    return render(request, "login.html")

  def post(self, request):
    username = request.POST["username"]
    password = request.POST["password"]

    if username and password:
      user = auth.authenticate(username=username, password=password)

      if user:
        auth.login(request, user)
        return redirect('expenses')
      messages.error(request, 'Invalid credentials, try again')
      return render(request, "login.html")
    messages.error(request, 'Please fill all fields')
    return render(request, "login.html")
  
class LogoutView(View):
  def post(self, request):
    auth.logout(request)
    return redirect('login')
    
