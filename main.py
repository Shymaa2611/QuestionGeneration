from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploaded_audio"


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



