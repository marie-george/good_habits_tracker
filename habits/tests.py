from rest_framework import status
from django.urls import reverse
from habits.models import Habit
from users.models import User
from rest_framework.test import APITestCase, APIClient


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='user@mail.ru',
            first_name='test',
            last_name='test',
            is_staff=False,
            is_superuser=False
        )

        self.user.set_password('123')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            action='test_action',
            place='test_place',
            starting_time='20:00:00',
            execution_time=120,
            interval=1,
            reward='test_reward',
            bound_habit=None,
            is_pleasant=False,
            is_public=False,
            creator=self.user
        )

    def test_get_list(self):
        """Проверка получения всего списка привычек"""

        response = self.client.get(reverse('habits:habits_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [
                 {'id': self.habit.id,
                  'action': self.habit.action,
                  'place': self.habit.place,
                  'starting_time': self.habit.starting_time,
                  'execution_time': self.habit.execution_time,
                  'interval': self.habit.interval,
                  'reward': self.habit.reward,
                  'is_pleasant': False,
                  'is_public': False,
                  'creator': 1,
                  'bound_habit': None}
             ]
             }
        )

    def test_get_public_list(self):
        """Проверка получения списка публичных привычек"""

        response = self.client.get(reverse('habits:public_habits_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(), [])

    def test_habit_create(self):
        """Проверка создания привычки"""

        response1 = self.client.post(
            reverse('habits:habits_create'),
            data={
                'action': 'test_action_2',
                'place': 'test_place',
                'starting_time': '10:00:00',
                'execution_time': 100,
                'interval': 1,
                'reward': 'test_reward',
                'bound_habit': '',
                'is_pleasant': False,
                'is_public': False,
                'creator': self.user.id
            }
        )

        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED
        )

        response2 = self.client.post(
            reverse('habits:habits_create'),
            data={
                'action': 'test_action_3',
                'place': 'test_place',
                'starting_time': '10:00:00',
                'execution_time': 100,
                'interval': 1,
                'reward': 'test_reward',
                'bound_habit': 'test_bound_habit', # не может быть одновремененно reward и bound_habit
                'is_pleasant': False,
                'is_public': False,
                'creator': self.user.id
            }
        )

        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        response3 = self.client.post(
            reverse('habits:habits_create'),
            data={
                'action': 'test_action_4',
                'place': 'test_place',
                'starting_time': '10:00:00',
                'execution_time': 100,
                'interval': 1,
                'reward': 'test_reward', # не может быть у приятной привычки
                'bound_habit': '',
                'is_pleasant': True,
                'is_public': False,
                'creator': self.user.id
            }
        )

        self.assertEqual(
            response3.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_habit_update(self):
        """Проверка редактирования привычки"""

        response = self.client.put(
            f'/habits/update/{self.habit.id}/',
            data={
                'action': 'test_action',
                'place': 'test_place',
                'starting_time': '10:00:00',
                'execution_time': 120,
                'interval': 1,
                'reward': 'test_reward',
                'bound_habit': '',
                'is_pleasant': False,
                'is_public': False,
                'creator': self.user.id
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_delete(self):
        """Проверка удаления привычки"""

        response = self.client.delete(f'/habits/delete/{self.habit.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Habit.objects.all().count(),
            0
        )

