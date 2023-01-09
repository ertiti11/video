from fastapi import FastAPI, Header
from fastapi.responses import Response
from os import getcwd, path
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PORTION_SIZE = 2048 * 2048

current_directory = getcwd() + "/"

@app.get("/video/{name_video}")
async def get_video(name_video: str, range: str = Header("bytes=0-")):
    # bytes=0-
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(start + PORTION_SIZE)

    # LEEMOS LA POSICION EXACTA DEL ARCHIVO

    with open(current_directory + name_video, "rb") as myfile:
        myfile.seek(start)
        data = myfile.read(end - start)
        size_video = str(path.getsize(current_directory + name_video))

        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{size_video}',
            'Accept-Ranges': 'bytes'
        }
        return Response(content=data, status_code=200, headers=headers, media_type="video/mp4")








# from local import get
# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# import os
# from pathlib import Path
# from fastapi import FastAPI
# from fastapi import Request, Response
# from fastapi import Header
# from fastapi.templating import Jinja2Templates
# app = FastAPI()


# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# CHUNK_SIZE = 1024*1024
# video_path = Path("C:\\Users\\vatit\\programacion\\react\\video\\Guest\\particulas.mp4")


# path = "C:\\Users\\vatit\\programacion\\react\\video\\Guest"

# @app.get("/")
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", context={"request": request})


# @app.get("/files")
# async def getfile():
#     return get()


# # @app.get("/video")
# # async def getvideo():
# #     file_path = os.path.join(path, "Particulas.mp4")
# #     return FileResponse(file_path)
# @app.get("/video")
# async def video_endpoint(range: str = Header(None)):
#     start, end = range.replace("bytes=", "").split("-")
#     start = int(start)
#     end = int(end) if end else start + CHUNK_SIZE
#     with open(video_path, "rb") as video:
#         video.seek(start)
#         data = video.read(end - start)
#         filesize = str(video_path.stat().st_size)
#         headers = {
#             'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
#             'Accept-Ranges': 'bytes'
#         }
#         return Response(data, status_code=206, headers=headers, media_type="video/mp4")