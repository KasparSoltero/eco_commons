from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import random

app = FastAPI()

app.mount("/front", StaticFiles(directory="front/public", html=True), name="front")
app.mount("/build", StaticFiles(directory="front/public/build", html=True), name="build")

@app.get("/")
async def front():
    return RedirectResponse(url="/front")

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.post("/upload_files")
async def upload_files(files: list[UploadFile]):
    print('here')
    print(files)
    print(files[0])
    print(type(files[0]))
    return RedirectResponse(url="/front", status_code=303)