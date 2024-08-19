from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

from django.db import models

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
