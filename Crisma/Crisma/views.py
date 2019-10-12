from django.http import HttpResponse
from django.shortcuts import render, redirect

def bemVindo(request):
    return render(request,'login/homepage.html')