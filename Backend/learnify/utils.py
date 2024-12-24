from google.cloud import vision
import io
import os
import fitz  # PyMuPDF
from PIL import Image
import json
from Backend import settings
class ExtractEngine:
    def __init__(self, file):
        self.file = file  # This can be either a file path or a file-like object
    
    
    def __str__(self):
        return self.text_result()
    
    def extract_text_from_pdf(self):
        doc = fitz.open(self.file)  # Open the PDF
        text = ""
        for page in doc:
            text += page.get_text()  # Extract text from each page
        return text or None


    def pdf_to_image(self):
        doc = fitz.open(self.file)
        images = []
        
        # Iterate through the pages
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Render page to a pixmap (image)
            pix = page.get_pixmap()
            
            # Convert pixmap to image
            img = Image.open(io.BytesIO(pix.tobytes()))
            images.append(img)
        
        return images
    
    def extract_text_from_image(self):
        # Initialize the Vision API client
        client = vision.ImageAnnotatorClient.from_service_account_json(os.path.join('cloud_key.json'))

        # Convert the image to a byte stream
        byte_io = io.BytesIO()
        image = self.pdf_to_image(self.file)
        image.save(byte_io, format='PNG')
        byte_io.seek(0)

        # Construct an image instance for Vision API
        vision_image = vision.Image(content=byte_io.read())

        # Perform text detection
        response = client.text_detection(image=vision_image)
        texts = response.text_annotations

        if texts:
            return texts[0].description  # Return the detected text
        else:
            return None

    # Function to convert PDF to images
    def text_result(self):
        text = self.extract_text_from_pdf()
        if text is not None:
            return text
        return self.extract_text_from_image()
    
class Course:
    def __init__(self,topic):
        self.topic = topic
        
def text_content():
    file_path = os.path.join(settings.MEDIA_ROOT, 'cos.json')
    with open(file_path,'r') as f:
        return json.loads(f.read())