#from django.test import TestCase
import fitz  # PyMuPDF
from google.cloud import vision
import io
import os

class extract_engine:
    def __init__(self,file):
        self.file= file
        
    def extract_text(self):
        doc = fitz.open(self.file)  # Open the PDF
        text = ""
        for page in doc:
            text += page.get_text()  # Extract text from each page
        return text or None
    
    def perform_ocr(self):
        # Initialize the Vision API client
        #client = vision.ImageAnnotatorClient()
        client = vision.ImageAnnotatorClient.from_service_account_json(os.path.join(self.file))

        # Load the image file
        with io.open(self.file, 'rb') as image_file:
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
                

        # Usage



