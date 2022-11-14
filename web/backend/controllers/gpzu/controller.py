from typing import List
from fastapi import APIRouter
from pydantic import StrictStr
from web.backend.model import USE_DB
from web.backend.loader import gpzu_service

router = APIRouter()


@router.get("/get_all_gpzu")
def get_all_gpzu():
    return gpzu_service.get_all_gpzus()


@router.post("/send_gpzu")
def send_gpzu(paths: List[StrictStr]):
    return gpzu_service.set_gpzus(paths)
