from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    DIFFICULT = 'Difficult'
    EXPERT = 'Export'
    CHOICES = (
        (BEGINNER, BEGINNER),
        (INTERMEDIATE, INTERMEDIATE),
        (DIFFICULT, DIFFICULT),
        (EXPERT, EXPERT)
    )
    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    height = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    training_level = models.CharField(max_length=100, choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    exercise = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.exercise


class EventData(models.Model):
    duration = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

