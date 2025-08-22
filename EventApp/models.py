from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    endTime = models.TimeField(default=datetime.time(17,00))
    created = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',null=True,blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date', '-time']
        verbose_name = "Event"
        verbose_name_plural = "Events"