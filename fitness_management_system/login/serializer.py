from rest_framework import serializers

from .models import User

class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

