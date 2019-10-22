from django.shortcuts import render
from .models import Usuario
# Create your views here.
def login_page(request):
    login = Usuario.objects.get(userID=request.POST['userID'])