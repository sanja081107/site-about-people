from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name room')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.TextField(verbose_name='Message')
    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Date')
    user = models.CharField(max_length=100, verbose_name='User name')
    room = models.CharField(max_length=100, verbose_name='Room name')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.value[:30]
