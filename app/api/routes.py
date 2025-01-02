from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.devops_api import AzureDevOpsAPI

router = APIRouter()

@router.get("/workitems")
def get_work_items():
    devops_api = AzureDevOpsAPI("org", "project", "pat")
    data = devops_api.get_work_items([1, 2, 3])
    return data