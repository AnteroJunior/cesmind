from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='schedule.index'),
    #path('/agendar', views.agendar, name='schedule.agendar'),
]
