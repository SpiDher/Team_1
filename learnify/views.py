from django.http import JsonResponse,HttpResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import ExtractEngine,text_content,quiz_result
import os
import random
from Backend import settings

@csrf_exempt
def gen_quiz(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES.get['file']
        level = request.POST.get('level', None)
        desc=request.POST.get('quiz-desc',None)

        # Create an instance and parse to the ExtractEngine
        if file:
            extractor = ExtractEngine(file)
            # Process the extracted text to generate a quiz (you can customize this as needed)
            quiz = quiz_result(extractor,level)
        else:
            quiz= quiz_result(desc,level)
        return JsonResponse(quiz, status=200)

    return JsonResponse({'error': 'No file provided'}, status=400)

@csrf_exempt
def home(request):
    return HttpResponse('Welcome')

@csrf_exempt
def content(request):
    course_data = text_content()
    return JsonResponse(course_data, status=200)

@csrf_exempt
def topic_material(request):
    filename= request.GET.get('filename')
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        file= open(file_path,'rb')
        try:
            response = FileResponse(file, as_attachment=True, filename=filename)
            return response
        except Exception as e:
            pass
    return JsonResponse({'error':'file not found'})

@csrf_exempt
def ran_quiz(request):
    level = request.GET.get('level')
    file_name = os.listdir(settings.MEDIA_ROOT)
    file_name.remove('quiz')
    file_name.remove('cos.json')
    ran_file= random.choice(file_name)
    extractor = ExtractEngine(os.path.join(settings.MEDIA_ROOT,ran_file))
    if level:
        quiz=quiz_result(extractor,level)
        return JsonResponse(quiz,status=200)
    quiz = quiz_result(extractor)
    return JsonResponse(quiz,status=200)

@csrf_exempt
def file_list(request):
    file_list = os.listdir(settings.MEDIA_ROOT)
    return JsonResponse({'Materials':file_list})


