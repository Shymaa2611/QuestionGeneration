from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from model.logic import generate_question
#,process_record,process_video,check_extension
#from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploaded_audio"


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_question")
async def get_questions(file: UploadFile = File(...)):
    """  questions=None
    filename = file.filename
    input=check_extension(filename)
    print("input is : ",input)
    if input=="audio":
        questions=process_record(file.file)
    elif input=="video":
        questions=process_video(file.file)
    else: """
    questions = generate_question(file.file)  
    return {"questions": questions}




        











