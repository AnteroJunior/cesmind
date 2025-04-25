from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='media.index'),
    path('adicionar', views.adicionar, name='media.adicionar'),
    path('<int:media_id>', views.media_detail, name='media.detail'),
    path('type/<str:type>', views.media_type, name='media.type'),
    path('user/<int:user_id>', views.media_user, name='media.user'),
]