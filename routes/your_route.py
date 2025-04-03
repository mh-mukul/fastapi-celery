from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, Depends

from config.logger import logger
from config.database import get_db
from utils.helper import ResponseHelper
from decorators.auth import api_key_required

from tasks import your_celery_task

router = APIRouter()
response = ResponseHelper()


class TestRequestBodoy(BaseModel):
    something: str = Field(None,)


@router.post("/test-celery")
@api_key_required
async def test_celery(request: Request, data: TestRequestBodoy, db: Session = Depends(get_db)):
    logger.info("Initiating celery task.")
    task = your_celery_task.apply_async(
        args=(data.something,)
    )
    return response.success_response(200, "success", data={"task_id": task.id})
