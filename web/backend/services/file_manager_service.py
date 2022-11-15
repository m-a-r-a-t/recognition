import asyncio
from tkinter import Tk, filedialog
import threading
from fastapi import WebSocket


class File_manager_service:
    def __init__(self, ws) -> None:
        self.ws = ws

    def open_file_manager(self):
        self.__run_file_manager()

    def __run_file_manager(self,):

        async def get_file_names_and_send(ws: WebSocket):
            root = Tk()
            root.withdraw()
            files = filedialog.askopenfilenames()
            root.destroy()
            print(files)
            await ws.send_json(files)

        thread = threading.Thread(target=asyncio.run, args=(get_file_names_and_send(self.ws),))

        thread.start()