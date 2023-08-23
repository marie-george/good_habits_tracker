from rest_framework import serializers
from habits.models import Habit
from habits.validators import double_reward_validator, pleasant_bound_validator, pleasant_not_rewarded_validator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [double_reward_validator, pleasant_bound_validator, pleasant_not_rewarded_validator]
