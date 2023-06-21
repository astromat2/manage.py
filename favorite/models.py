from register.models import User
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    '''модель для хранения информации об избранных тренировках для каждого пользователя'''
    users = models.ManyToManyField(User, related_name='favorite_exercises', blank=True)
