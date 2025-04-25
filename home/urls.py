from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home.index'),
    path('login', views.login, name='home.login'),
    path('logout', views.logout, name='home.logout'),
    path('create', views.create, name='home.create'),
]
