from login import models
import datetime


def generate_event_data(user_id, exercise_id):
    """
    Create a new event record for update an existing event. Once a user watch the video during the same day,
    the state exercise_times of event will be increased by one. If it's the first time that the user watches the video,
    then a new event record will be created with 'exercise_times' default to one.
    """
    d = datetime.date.today()
    event = models.EventData.objects.filter(user_id=user_id, exercise_id=exercise_id).latest('created_at')
    if not event or event.created_at < d:
        models.EventData.objects.create(user_id=user_id, exercise_id=exercise_id, exercise_times=1)
    else:
        event.exercise_times += 1
        event.save()


def calculate_calories(user_id):
    total_calories = 0
    d = datetime.date.today()
    events = models.EventData.objects.filter(user_id=user_id, created_at=d).values()
    for event in events:
        times = event['exercise_times']
        exercise_id = event['exercise_id']
        exercise_obj = models.Exercise.objects.get(id=exercise_id)
        calorie = exercise_obj.calories
        total_calories += calorie * times
    return total_calories


def get_event_history(user_id):
    events = models.EventData.objects.filter(user_id=user_id).values()
    return events




