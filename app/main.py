from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
from pipeline import process_image

load_dotenv()

app = FastAPI()

@app.post("/extract")
async def extract_marksheet(file: UploadFile):
    result = process_image(file)
    return result
