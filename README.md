# QuizGen

QuizGen is a web application designed for generating questions based on input documents, leveraging a fine-tuned T5 model on the SQuAD dataset. This application is built using FastAPI, HTML, CSS, and JavaScript, and utilizes Jinja2 for rendering templates.

## DEMO


## Features

- Upload PDF documents, videos, or audio files to generate relevant questions.
- Fine-tuned T5 model on the SQuAD dataset for high-quality question generation.
- User-friendly interface with responsive design.
- Built using FastAPI for backend functionality and Jinja2 for frontend rendering.

## Technologies Used

- **FastAPI**: For building the web application.
- **T5**: For natural language processing and question generation.
- **Hugging Face Transformers**: For model management and fine-tuning.
- **HTML/CSS/JavaScript**: For frontend development.
- **Jinja2**: For rendering HTML templates.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/Shymaa2611/QuestionGeneration.git
cd QuestionGeneration
```

### Install Dependencies
```bash
pip install -r requirements.txt

```

### Download the SQuAD Dataset

You can download the SQuAD dataset from Hugging Face using the following command:
```bash
pip install datasets

```
```python
from datasets import load_dataset
dataset = load_dataset("rajpurkar/squad")
```


### Running the Application
- Start the FastAPI server:
```bash
uvicorn main:app --reload

```
- Open your browser and navigate to http://127.0.0.1:8000.
- Use the web interface to upload files and generate questions.