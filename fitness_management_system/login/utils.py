from login import models
from django.core.exceptions import ObjectDoesNotExist
import datetime


def generate_event_data(user_id, exercise_id):
    """
    Create a new event record for update an existing event. Once a user watch the video during the same day,
    the state exercise_times of event will be increased by one. If it's the first time that the user watches the video,
    then a new event record will be created with 'exercise_times' default to one.
    """
    d = datetime.date.today()
    try:
        event = models.EventData.objects.get(user_id=user_id, exercise_id=exercise_id, created_at=d)
    except ObjectDoesNotExist:
        event = None

    if not event:
        models.EventData.objects.create(user_id=user_id, exercise_id=exercise_id, exercise_times=1)
    else:
        event.exercise_times += 1
        event.save()


def calculate_calories_duration(user_id):
    total_calories = 0
    total_duration = 0
    d = datetime.date.today()
    events = models.EventData.objects.filter(user_id=user_id, created_at=d).values()
    for event in events:
        times = event['exercise_times']
        exercise_id = event['exercise_id']
        exercise_obj = models.Exercise.objects.get(id=exercise_id)
        calorie = exercise_obj.calories
        duration = exercise_obj.duration
        total_calories += calorie * times
        total_duration += duration * times
    return total_calories, total_duration


def get_event_history(user_id):
    events = models.EventData.objects.filter(user_id=user_id).values()
    return events
