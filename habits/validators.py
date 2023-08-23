from rest_framework.serializers import ValidationError


def double_reward_validator(data):
    if data.get('bound_habit') and data.get('reward'):
        raise ValidationError('Вы не можете указать одновременно "вознаграждение" и "приятную привычку". Выберите что-то одно')


def pleasant_bound_validator(data):
    if data.get('bound_habit') and not data.get('bound_habit').is_pleasant:
        raise ValidationError('Вы можете добавлять в связанные привычки только приятные привычки.')


def pleasant_not_rewarded_validator(data):
    if data.get('is_pleasant') and (data.get('reward') or data.get('bound_habit')):
        raise ValidationError('Приятные привычки не могут иметь вознаграждение или связанную привычку.')

