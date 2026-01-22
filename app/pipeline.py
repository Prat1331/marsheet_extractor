# pipeline.py
import tempfile
from app.ocr import extract_text
from app.llm import extract_structured_data

def process_image(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_file.file.read())
        temp_path = temp.name

    text = extract_text(temp_path)
    structured_json = extract_structured_data(text)

    return {
        "raw_text": text,
        "structured_data": structured_json
    }
