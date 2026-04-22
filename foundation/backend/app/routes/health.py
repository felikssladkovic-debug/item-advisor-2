from fastapi import APIRouter, Depends
from pymongo.database import Database

from app.dependencies import get_database
from app.schemas.common import ApiSuccess
from app.schemas.health import HealthData

router = APIRouter(tags=["health"])


@router.get("/health", response_model=ApiSuccess[HealthData])
async def health(database: Database = Depends(get_database)) -> ApiSuccess[HealthData]:
    database.command("ping")
    return ApiSuccess(
        data=HealthData(
            status="ok",
            database="ok",
        )
    )
