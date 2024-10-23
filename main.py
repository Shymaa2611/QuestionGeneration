from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from model.logic import generate_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploaded_audio"


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_question")
async def get_questions(pdf_file: UploadFile = File(...)):
    questions = generate_question(pdf_file.file)  
    return {"questions": questions}



if __name__=="__main__":
    file_path="/home/notebook/Downloads/sodapdf-converted.pdf"
    print("========================= Questions ===========================")
    print(generate_question(file_path))
        











