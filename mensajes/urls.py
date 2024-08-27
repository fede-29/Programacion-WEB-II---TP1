from django.urls import path
from . import views

urlpatterns = [
    path('recibidos/', views.recibidos, name='recibidos'),
]