from django.urls import path
from .views import encontroHome

urlpatterns = [
    path('', encontroHome, name='encontro'),

]