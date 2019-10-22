from django.http import HttpResponse
from django.shortcuts import render, redirect

def homePage(request):
    return render(request,'login/homepage.html')