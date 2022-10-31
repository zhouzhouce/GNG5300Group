from django.contrib import admin
from .models import User
from .models import UserProfile
from .models import Exercise
from .models import EventData

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Exercise)
admin.site.register(EventData)