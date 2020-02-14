from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets

from Profile import views

urlpatterns = [
    re_path(r'estadoCivil_list/$', views.EstadoCivilList.as_view()),
    re_path(r'estado_list/$', views.EstadoList.as_view()),
    re_path(r'ocupacion_list/$', views.OcupacionList.as_view()),
    re_path(r'genero_list/$', views.GeneroList.as_view()),
    re_path(r'ciudad_list/$', views.CiudadList.as_view()),
    re_path(r'profile_list/$', views.ProfileList.as_view()),
]