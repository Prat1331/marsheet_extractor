# ocr.py
import cv2
import easyocr
import gc

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path)
    img = cv2.resize(img, None, fx=1.5, fy=1.5)  # reduce from 2x

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(
        Image.fromarray(thresh),
        config="--psm 6"
    )

    del img, gray, thresh
    gc.collect()

    return text

