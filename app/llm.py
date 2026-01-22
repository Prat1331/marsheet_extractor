# llm.py
import os
import google.generativeai as genai
from schemas import SCHEMA, build_prompt

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def extract_structured_data(text: str) -> str:
    prompt = build_prompt(text)
    response = model.generate_content(prompt)
    return response.text
