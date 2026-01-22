def process_image(image):
    text = extract_text(image)
    data = extract_json(text)
    return data
