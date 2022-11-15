from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import StrictStr, StrictInt
from web.backend.model import USE_DB
from web.backend.loader import gpzu_service

router = APIRouter()


@router.get("/get_all_gpzu")
def get_all_gpzu():
    try:
        return gpzu_service.get_all_gpzus()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/send_gpzu")
def send_gpzu(paths: List[StrictStr]):
    try:
        return gpzu_service.calc_and_save_gpzus(paths)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/export_to_excel")
def send_gpzu(ids: List[StrictInt]):
    try:
        return gpzu_service.export_to_excel(ids)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
