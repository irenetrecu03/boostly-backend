import logging
import time
from celery import shared_task
from .models import Habit, User

logger = logging.getLogger(__name__)

@shared_task(name='get_habits')
def get_habit_list(user_id):
    try:
        user = User.objects.get(id=user_id)
        habits = Habit.objects.filter(user=user)
        time.sleep(1)

        logger.info(f"Habits retrieved")
        return habits
    except Exception as e:
        logger.error(f"Failed to fetch habits: {e}")
        raise

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
def delete_habit(habit_id):
    try:
        Habit.objects.filter(id=habit_id).delete()
        time.sleep(1)

        logger.info(f"Habit deleted: {habit_id}")
        return 'Habit deleted'
    except Exception as e:
        logger.error(f"Failed to delete habit: {e}")
        raise

