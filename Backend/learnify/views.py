from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ai.use_ai_gen_quiz import quiz_engine
from .utils import extract_text_from_pdf

# Create your views here.
@csrf_exempt
def gen_quiz(request):
    file= request.FILES('file')
    level = request.get('level')
    #extract tetxt from pdf
    file_content =file.read()
    ocr=extract_text_from_pdf(file_content)
    quiz = quiz_engine(ocr,level)
    return quiz
                                    