from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Student(models.Model):
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30)
#     last_name= models.CharField(max_length=30)
#     email = models.CharField(max_length=50,unique=True)
#     course = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     date_of_birth = models.DateField()
