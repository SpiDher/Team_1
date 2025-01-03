import io
import os
import fitz  # PyMuPDF
from PIL import Image
import json
from Backend import settings
from datetime import datetime
import random, asyncio
from .ai.ai_gen_quiz_model import quiz_engine
import logging

logging.basicConfig(level=logging.info)


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
        return text[:40000] or None  # Limit the text to 25000 characters


#def restructure_quiz_data(input_data):
    """
    Restructures the input quiz data to the desired format.

    Args:
        input_data (dict): The original quiz data containing name and questions.

    Returns:
        dict: Restructured quiz data in the desired format.
    """
    # Extract the name and questions from the input
    #name = input_data.get("name", "Quiz")
    #questions = input_data.get("questions", [])

    # Restructure the questions
    #restructured_questions = []
    #for question in questions:
        #restructured_questions.append(
           # {
   #             "question": question["question"],
          #      "options": question["options"],
      #          "correct": question["correctAnswer"],
          #      "feedback": question["feedBack"],
          #  }
   #     )

    # Build the final structure
   # output_data = {
      #  "name": name,
      #  "time": 1800,  # Default time set to 1800 seconds (30 minutes)
        #"questions": restructured_questions,
   # }

   # return output_data


# get json file content
def text_content():
    file_path = os.path.join(settings.MEDIA_ROOT, "cos.json")
    with open(file_path, "r") as f:
        return json.loads(f.read())


def save_quiz(object):
    date_time = datetime.now()
    time = date_time.time()
    file_path = os.path.join(
        settings.MEDIA_ROOT, "quiz", f'quiz_{time.strftime("%H-%M")}.json'
    )
    if file_list := len(os.listdir(os.path.join(settings.MEDIA_ROOT, "quiz"))) != 10:
        with open(file_path, "w") as file:
            json.dump(object, file, indent=4)
    return True


def contingency():
    logging.info("No quiz generated\n Switching to contingency quiz")
    quiz_list = os.listdir(os.path.join(settings.MEDIA_ROOT, "quiz"))
    ran_choice = random.choice(quiz_list)
    file_path = os.path.join(settings.MEDIA_ROOT, "quiz", ran_choice)
    with open(file_path, "r", newline="") as file:
        return json.loads(file.read())


def quiz_result(text, level="MEDIUM"):
    quiz = asyncio.run(quiz_engine(extracted_text=text, difficult_level=level))
    if quiz is not None:
        # save_quiz(quiz) #Only remove this comment in development
        logging.log(logging.INFO, "Quiz generated successfully")
        return restructure_quiz_data(quiz)
    return contingency()
