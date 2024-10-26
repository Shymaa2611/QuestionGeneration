from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from model.logic import generate_question,process_record,process_video,check_extension

app = FastAPI()
templates = Jinja2Templates(directory="templates")
UPLOAD_FOLDER = "uploaded_audio"


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_question")
async def get_questions(file: UploadFile = File(...)):
    questions=""
    input=check_extension(file.filename)
    if input=="audio":
        questions=process_record(file.file)
    elif input=="video":
        questions=process_video(file.file)
    else: 
        questions = generate_question(file.file)  
    return {"questions": questions}




        











