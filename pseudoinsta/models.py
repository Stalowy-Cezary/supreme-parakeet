from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title