from inference import inference
from PyPDF2 import PdfReader 

def split_pdf_to_chunks(text: str) -> list[str]:
    """
    This function splits a given text into smaller chunks of a specified length.

    Parameters:
    text (str): The input text to be split into chunks.

    Returns:
    list[str]: A list of chunks, where each chunk is a substring of the input text.
    """
    chunks = []
    chunk_len = 1000
    for i in range(0, len(text), chunk_len):
        chunks.append(text[i:i+chunk_len])
    return chunks

def extract_text_from_file(pdf_path: str) -> str:
    """
    This function extracts text from a PDF file using the PyPDF2 library.

    Parameters:
    pdf_path (str): The path to the PDF file.

    Returns:
    str: The extracted text from the PDF file.
    """
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + " "
    return text

def generate_question(pdf_path:str):    
    text = extract_text_from_file(pdf_path)
    chunks = split_pdf_to_chunks(text)
    questions = [inference(context) for context in chunks]
    return questions
    

    