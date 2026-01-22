# ocr.py
import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    results = reader.readtext(img)
    text = "\n".join([r[1] for r in results])

    return text
