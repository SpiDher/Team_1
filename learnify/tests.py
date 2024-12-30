import sys
sys.path.append('..')
import os
from Backend import settings
from learnify.utils import save_quiz,text_content
import json

# from datetime import datetime
# date_time = datetime.now()
# time = date_time.time()
# print(time.strftime('%H-%M'))
# l_ist=os.listdir(settings.MEDIA_ROOT)
# file_name= [file for file in l_ist if file not in ['cos.json','quiz']]
# file_list = [file for file in os.listdir(settings.MEDIA_ROOT) if file not in ['quiz']]
# print(file_name,file_list)

dir= os.listdir(os.path.join(settings.MEDIA_ROOT,'quiz'))
file_path = lambda file: os.path.join(settings.MEDIA_ROOT,'quiz',file)
    
def location(file_path,object):
    with open(file_path,'w',newline='') as file:
        json.dump(object,file,indent=4)
    print('Done')

def restructure_quiz_data(input_data):
    """
    Restructures the input quiz data to the desired format.
    
    Args:
        input_data (dict): The original quiz data containing name and questions.
    
    Returns:
        dict: Restructured quiz data in the desired format.
    """
    # Extract the name and questions from the input
    name = input_data.get("name", "Quiz")
    questions = input_data.get("questions", [])
    
    # Restructure the questions
    restructured_questions = []
    for question in questions:
        restructured_questions.append({
            "question": question["question"],
            "options": question["options"],
            "correct": question["correctAnswer"],
            "feedback": question["feedBack"]
        })
    
    # Build the final structure
    output_data = {
        "name": name,
        "time": 1800,  # Default time set to 1800 seconds (30 minutes)
        "questions": restructured_questions
    }
    
    return output_data
for path in dir:
    file_dir=file_path(path)
    with open(file_dir,'r',newline='') as f:
        data= json.loads(f.read())
    res_data=restructure_quiz_data(data)
    print(json.dumps(res_data,indent=4))
    location(file_dir,res_data)
    