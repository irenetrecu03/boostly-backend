import logging
import time
from celery import shared_task
from .models import Habit, User
from .serializers import HabitSerializer

logger = logging.getLogger(__name__)


@shared_task(name='create_habit')
def create_habit(user_id, habit_data):
    try:
        user = User.objects.get(id=user_id)
        habit = Habit.objects.create(user=user, **habit_data)
        time.sleep(1)

        logger.info(f"Habit created: {habit}")
        return 'Habit created'
    except Exception as e:
        logger.error(f"Failed to create habit: {e}")
        raise

@shared_task(name='delete_habit')
def delete_habit(habit_id, user_id):
    try:
        user = User.objects.get(id=user_id)
        habit = Habit.objects.filter(id=habit_id, user=user)

        if habit.exists():
            habit.delete()
            time.sleep(1)

            logger.info(f"Habit deleted: {habit_id}")
            return 'Habit deleted'

        else:
            logger.error(f"Habit not found: {habit_id}")
            return 'Habit not found or unauthorized'

    except Exception as e:
        logger.error(f"Failed to delete habit: {e}")
        raise

@shared_task(name='update_habit')
def update_habit(habit_id, habit_data, user_id):
    try:
        user = User.objects.get(id=user_id)
        habit = Habit.objects.filter(id=habit_id, user=user)

        if habit.exists():
            habit.update(**habit_data)
            time.sleep(1)

            logger.info(f"Habit updated: {habit_id}")
            return 'Habit updated'
        else:
            logger.error(f"Habit not found: {habit_id}")
            return 'Habit not found or unauthorized'

    except Exception as e:
        logger.error(f"Failed to update habit: {e}")
        raise

