from django.db import models
from django.contrib.auth.models import User
class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)  # Not recommended for real-world applications

    def __str__(self):
        return self.username
