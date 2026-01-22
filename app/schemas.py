# schemas.py
SCHEMA = """
{
  "candidate": {
    "name": {"value": "", "confidence": 0},
    "father_name": {"value": "", "confidence": 0},
    "mother_name": {"value": "", "confidence": 0},
    "roll_no": {"value": "", "confidence": 0},
    "board": {"value": "", "confidence": 0},
    "exam": {"value": "", "confidence": 0},
    "year": {"value": "", "confidence": 0},
    "school": {"value": "", "confidence": 0}
  },
  "subjects": [
    {
      "subject": {"value": "", "confidence": 0},
      "marks": {"value": 0, "confidence": 0},
      "grade": {"value": "", "confidence": 0}
    }
  ],
  "overall_result": {"value": "", "confidence": 0}
}
"""

def build_prompt(text: str) -> str:
    return f"""
You are an expert marksheet parser.

Extract:
- Student name
- Father name
- Mother name
- Roll number
- Board
- Exam name
- Year
- School
- Subjects with marks and grade
- Overall result

Text:
{text}

Rules:
- Missing → empty string
- Confidence 0 to 1
- Return ONLY valid JSON in this schema:

{SCHEMA}
"""
