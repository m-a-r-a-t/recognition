from typing import Union
import uvicorn
import webbrowser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from web.backend.controllers.gpzu.controller import router as gpzu_controller
from web.backend.controllers.file_manager.controller import router as file_manager_controller
#! from tkinter import Tk, filedialog

# !Tk().withdraw()

#! print(filedialog.askopenfilename())

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gpzu_controller)
app.include_router(file_manager_controller)

app.mount("/", StaticFiles(directory="web/backend/public", html=True), name="static")


def serve():
    """Serve the web application."""
    # webbrowser.open('http://127.0.0.1:8000', new=2)
    uvicorn.run(app)


if __name__ == "__main__":
    serve()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
