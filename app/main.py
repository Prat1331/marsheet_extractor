from fastapi import FastAPI, UploadFile
from pipeline import process_image

app = FastAPI()

@app.post("/extract")
async def extract_marksheet(file: UploadFile):
    result = process_image(file)
    return result
