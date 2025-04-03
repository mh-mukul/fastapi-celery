from config.logger import logger
from celery_config import celery_app


# Celery Task
@celery_app.task
def your_celery_task(data=None):
    logger.info(f"Celery task is working: {data}")
    return True
