📄 Marksheet Information Extraction API

An end-to-end OCR + LLM powered FastAPI application that extracts structured information from marksheet images (PNG/JPG/JPEG).

The system processes an uploaded marksheet image, performs OCR to extract text, and then uses a Large Language Model (LLM) to convert the raw text into structured JSON data.

🚀 Features

Upload marksheet images via REST API

OCR preprocessing using OpenCV

Text extraction using OCR engine

Structured data extraction using LLM (Gemini)

JSON output with student details, subjects, and results

Interactive Swagger UI (/docs)

Deployed as a public API

🏗️ Architecture Overview
Client (Image Upload)
        |
        v
FastAPI (/extract endpoint)
        |
        v
OCR Module (Image → Text)
        |
        v
LLM Module (Text → Structured JSON)
        |
        v
JSON Response

📁 Project Structure
marsheet_extractor/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── ocr.py           # OCR logic
│   ├── llm.py           # LLM integration
│   ├── pipeline.py      # End-to-end processing
│   └── schemas.py       # JSON schema + prompt
├── notebooks/
│   └── Untitled8.ipynb  # OCR & prompt experimentation
├── requirements.txt
├── .gitignore
└── README.md

🧠 OCR Approach

Image preprocessing:

Resize (2× upscaling)

Grayscale conversion

Noise reduction

OCR engine extracts text from the processed image

OCR output is saved and passed to the LLM

OCR experimentation and tuning were done in the provided Jupyter notebook.

🤖 LLM-Based Information Extraction

Uses Gemini (LLM) to parse noisy OCR text

Carefully designed prompt + schema

Extracts:

Student name

Parent details

Roll number

Board / University

Exam & year

Subjects with marks and grades

Overall result

Returns strict JSON output

📡 API Endpoints
POST /extract

Upload a marksheet image and receive extracted data.

Request

Content-Type: multipart/form-data

Body: Image file

Response

{
  "raw_text": "... OCR output ...",
  "structured_data": "{ ... JSON from LLM ... }"
}

🧪 API Documentation (Swagger)

Interactive API docs available at:

/docs


When deployed, use the public URL:

https://<your-app-name>.onrender.com/docs

⚙️ Local Setup
1️⃣ Clone Repository
git clone https://github.com/Prat1331/marsheet_extractor.git
cd marsheet_extractor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Environment Variable
export GEMINI_API_KEY=your_api_key   # Linux/Mac
set GEMINI_API_KEY=your_api_key      # Windows

4️⃣ Run Application
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

☁️ Deployment

Deployed on Render

Uses environment variables for API keys

Start command:

uvicorn app.main:app --host 0.0.0.0 --port $PORT

🔐 Security

API keys are stored as environment variables

.env file is ignored using .gitignore

No secrets committed to repository

⚠️ Limitations

OCR accuracy depends on image quality

Handwritten marksheets are not supported

LLM output may vary for extremely noisy OCR text

No database persistence (stateless API)

🔮 Future Improvements

Confidence scoring for extracted fields

Multi-language OCR support

PDF upload support

Batch processing

Database integration

Authentication & rate limiting

📌 Notes

The notebook in /notebooks was used for experimentation and tuning

Production logic is fully refactored into modular Python files

Designed following clean architecture principles

👤 Author

Prath
