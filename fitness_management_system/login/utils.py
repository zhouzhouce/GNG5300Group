from django.db import models
from django_mysql.models import EnumField


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
