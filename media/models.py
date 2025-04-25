from django.db import models
from home.models import User

# Create your models here.
class Media(models.Model):
    mediaType = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnails/')
    file = models.FileField(upload_to='media/files/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)