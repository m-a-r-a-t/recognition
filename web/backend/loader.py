from web.backend.services.gpzu_service import Gpzu_Service
from web.backend.services.file_manager_service import File_manager_service

gpzu_service = Gpzu_Service()
file_manager_service = File_manager_service(None)  # нужен еще sse сервер
