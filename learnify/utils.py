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
        return self.extract_text_from_pdf()
    
    def extract_text_from_pdf(self):
        doc = fitz.open(self.file)  # Open the PDF
        text = ""
        for page in doc:
            text += page.get_text()  # Extract text from each page
        return text or None

    
#get json file content
def text_content():
    file_path = os.path.join(settings.MEDIA_ROOT, 'cos.json')
    with open(file_path,'r') as f:
        return json.loads(f.read())