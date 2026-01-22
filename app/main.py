from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import os
from app.pipeline import process_image

# Load .env from parent directory (project root)
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
# Also try loading from current directory as fallback
load_dotenv()

app = FastAPI()

@app.post("/extract")
async def extract_marksheet(file: UploadFile):
    result = process_image(file)
    return result
