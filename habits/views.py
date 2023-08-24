from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.services import set_schedule


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()
        set_schedule(new_habit)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
