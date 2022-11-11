from django.db import models
from login import utils
from django_mysql.models import EnumField


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    # user = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100, default='UNDEFINED')
    name = models.CharField(max_length=100, unique=True)
    age = EnumField(choices=utils.AgeEnum.choices, default='UNDEFINED')
    gender = EnumField(choices=utils.GenderEnum.choices, default='UNDEFINED')
    level = EnumField(choices=utils.LevelEnum.choices, default='ENTRY')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    exercise_title = EnumField(choices=utils.ExerciseTitleEnum.choices, default='HITT')
    level = EnumField(choices=utils.LevelEnum.choices, default='ENTRY')
    duration = models.FloatField(default=0)
    calories = models.IntegerField(default=0)
    link = models.URLField(max_length=200, default='https://www.youtube.com/')

    def __str__(self):
        return self.exercise_title


class EventData(models.Model):
    user_id = models.CharField(max_length=100, default='UNDEFINED')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    exercise_times = models.IntegerField()

    def __str__(self):
        return 'Event_' + self.id




