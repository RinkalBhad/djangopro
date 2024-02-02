from rest_framework import serializers
from .models import*

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=userdata
        fields="__all__"