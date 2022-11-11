from django.db import models
from django_mysql.models import EnumField
import datetime


# Create your models here.
class LevelEnum(models.TextChoices):
    ENTRY = 'ENTRY'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'


class GenderEnum(models.TextChoices):
    FEMALE = 'FEMALE'
    MALE = 'MALE'
    UNDEFINED = 'UNDEFINED'


class AgeEnum(models.TextChoices):
    AGE_RANGE_0_29 = 'AGE_RANGE_0_29'
    AGE_RANGE_30_40 = 'AGE_RANGE_30_40'
    AGE_RANGE_40_50 = 'AGE_RANGE_40_50'
    AGE_ABOVE_50 = 'AGE_ABOVE_50'
    UNDEFINED = 'UNDEFINED'


class ExerciseTitleEnum(models.TextChoices):
    HIIT = 'HITT'
    YOGA = 'YOGA'
    CARDIO = 'CARDIO'
    BOOTY = 'BOOTY'
    AB_WORKOUT = 'AB_WORKOUT'
    WAIST = 'WAIST'
    CIRCUIT = 'CIRCUIT'
    STRENGTH = 'STRENGTH'
    FAT_BURNING = 'FAT_BURNING'


class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    # user = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100, default='UNDEFINED')
    name = models.CharField(max_length=100, unique=True)
    age = EnumField(choices=AgeEnum.choices, default='UNDEFINED')
    gender = EnumField(choices=GenderEnum.choices, default='UNDEFINED')
    level = EnumField(choices=LevelEnum.choices, default='ENTRY')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    exercise_title = EnumField(choices=ExerciseTitleEnum.choices, default='HITT')
    level = EnumField(choices=LevelEnum.choices, default='ENTRY')
    duration = models.FloatField(default=0)
    calories = models.IntegerField(default=0)
    link = models.URLField(max_length=200, default='https://www.youtube.com/')

    def __str__(self):
        return self.exercise_title


class EventData(models.Model):
    user_id = models.CharField(max_length=100, default='UNDEFINED')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    exercise_times = models.IntegerField()
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return 'Event_' + self.id
