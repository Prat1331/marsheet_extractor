# ocr.py
import cv2
import pytesseract
import tempfile
from PIL import Image

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path)

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    thresh = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    text = pytesseract.image_to_string(
        Image.fromarray(thresh),
        config="--psm 6"
    )
    return text
