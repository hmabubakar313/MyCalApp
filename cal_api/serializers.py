from cal_count.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BreakfastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breakfast
        fields = '__all__'



class LunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lunch
        fields = '__all__'



class DinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinner
        fields = '__all__s'
