from typing import List
from fastapi import APIRouter, WebSocket
from pydantic import StrictStr
from web.backend.loader import file_manager_service
from web.backend.services.file_manager_service import File_manager_service
router = APIRouter()


@router.websocket("/ws")
async def open_file_manager(ws: WebSocket):
    await ws.accept()

    file_manager_service = File_manager_service(ws)
    while True:
        try:
            data = await ws.receive_json()
            print(data)
            if data["type"] == "open_file_manager":
                print("===============================", data)
                file_manager_service.open_file_manager()
            # await ws.send_text(f"Message text was: {data}")
        except Exception as e:
            print("Websocket closed", e)
            # await ws.close()
            break
