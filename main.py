from local import get
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

path = "C:\\Users\\MEDAC\\Desktop\\Programacion\\react\\video\\Guest"
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/files")
async def getfile():
    return get()


@app.get("/video")
async def getvideo():
    file_path = os.path.join(path, "Particulas.mp4")
    return FileResponse(file_path, media_type="mp4")