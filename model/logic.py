from inference import inference
from PyPDF2 import PdfReader 
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from transformers import pipeline
from model.process_input import clean
from tempfile import NamedTemporaryFile
import numpy as np

def split_text_to_chunks(text: str) -> list[str]:
    chunks = []
    chunk_len = 150
    for i in range(0, len(text), chunk_len):
        chunks.append(text[i:i+chunk_len])
    return chunks

def extract_text_from_file(pdf_path: str) -> str:
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + " "
    return text


def check_extension(input:str):
    if input.endswith(".pdf"):
       return "pdf"
    elif input.endswith(".mp4"):
       return "video"
    return "audio"
 
def generate_question(pdf_path:str):    
    text = extract_text_from_file(pdf_path)
    chunks = split_text_to_chunks(text)
    questions = [inference(clean(context)) for context in chunks]
    return questions
    

def splite_audio_segments(audio_path:str,segment_duration_ms=15):
    audio = AudioSegment.from_file(audio_path)
    num_segments = len(audio) // segment_duration_ms + (1 if len(audio) % segment_duration_ms > 0 else 0)
    segments = []
    for i in range(num_segments):
        start_time = i * segment_duration_ms
        end_time = start_time + segment_duration_ms
        segment = audio[start_time:end_time]
        segments.append(segment)
    return segments

def convert_audio_to_text(segment):
    pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
    raw_audio = np.array(segment.get_array_of_samples())
    audio_array = raw_audio.astype(np.float32) / 32768.0
    if segment.channels > 1:
        audio_array = audio_array.reshape((-1, segment.channels)).mean(axis=1)
    result = pipe(audio_array, return_timestamps=False)  
    return result["text"] 


def extract_audio_from_video(video_file, audio_file="output.wav"):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    audio.close()
    video.close()

    
def process_record(file):
    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name
    segments = splite_audio_segments(temp_file_path)
    full_text=""
    for segment in segments:
        text = convert_audio_to_text(segment.export("temp.wav", format="wav"))
        full_text += text
    chunks=split_text_to_chunks(full_text)
    questions = [inference(context) for context in chunks]
    return questions


def process_video(file):
    with NamedTemporaryFile(delete=False, suffix=".mp4") as video_temp_file:
        video_temp_file.write(file.read())
        video_temp_file_path = video_temp_file.name
    extract_audio_from_video(video_temp_file_path)
    with open("output.wav", "rb") as audio_file:
        questions = process_record(audio_file)
    return questions
    




    