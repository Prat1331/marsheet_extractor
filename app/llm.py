# llm.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.schemas import SCHEMA, build_prompt

# Load .env from parent directory (project root)
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
# Also try loading from current directory as fallback
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def extract_structured_data(text: str) -> str:
    prompt = build_prompt(text)
    response = model.generate_content(prompt)
    return response.text
