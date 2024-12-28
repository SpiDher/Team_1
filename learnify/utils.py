import io
import os
import fitz  # PyMuPDF
from PIL import Image
import json
from Backend import settings
from datetime import datetime
import random,asyncio
from .ai.ai_gen_quiz_model import quiz_engine
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

def save_quiz(object):
    date_time = datetime.now()
    time = date_time.time()
    file_path = os.path.join(settings.MEDIA_ROOT,'quiz',f'quiz_{time.strftime("%H-%M")}.json')
    if file_list:= len(os.listdir(os.path.join(settings.MEDIA_ROOT,'quiz')))!=10:
        with open(file_path,'w') as file:
            json.dump(object,file,indent=4)
    return True

def contingency():
    quiz_list= os.listdir(os.path.join(settings.MEDIA_ROOT,'quiz'))
    ran_choice =random.choice(quiz_list)
    file_path = os.path.join(settings.MEDIA_ROOT,'quiz',ran_choice)
    with open(file_path,'r',newline='') as file:
        return json.loads(file.read())
    
def quiz_result(text,level='MEDIUM'):
    quiz = asyncio.run(quiz_engine(extracted_text=text,difficult_level=level))
    if quiz is not None:
        #save_quiz(quiz) #Only remove this comment in development 
        return quiz
    return contingency()
    