from google.cloud import vision
import io
import os

def extract_text_from_image(image_path):
    # Initialize the Vision API client
    #client = vision.ImageAnnotatorClient()
    client = vision.ImageAnnotatorClient.from_service_account_json(os.path.join('cloud_key.json'))

    # Load the image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Construct an image instance
    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description  # Return the detected text
    else:
        return "No text detected."


def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    '''images = convert_from_path(pdf_path)
    all_text = ""

    # Process each image page
    for i, image in enumerate(images):
        # Save the image temporarily
        image_path = f"page_{i + 1}.jpg"
        image.save(image_path, "JPEG")

        # Extract text from the image
        text = extract_text_from_image(image_path)
        all_text += f"Page {i + 1}:\n{text}\n\n"

    return all_text

# Usage
pdf_path = os.path.join('pdf-test.pdf')
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)'''
