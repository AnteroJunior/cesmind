from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard.index'),
    path('assume/<int:schedule_id>', views.assume, name='dashboard.assume'),
]