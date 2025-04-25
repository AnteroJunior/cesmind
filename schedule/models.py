from django.db import models
from home.models import User

# Create your models here.
class Schedule(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    period = models.CharField(max_length=20)
    reason = models.TextField()
    availability = models.CharField(max_length=100)
    professional = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)