from habits.apps import HabitsConfig
from django.urls import path

from habits.views import HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, HabitListAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits_delete'),
    path('', HabitListAPIView.as_view(), name='habits_list'),
    path('public/', PublicHabitListAPIView.as_view(), name='public_habits_list')
]

