from django.http import JsonResponse,HttpResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import ExtractEngine,text_content,quiz_result
import os
import random
from Backend import settings

@csrf_exempt
def gen_quiz(request):
    get_param = lambda key: request.POST.get(key, None) or request.GET.get(key, None)
    if get_param('file') or get_param('content'):
        file = request.FILES.get('file',None)
        level = get_param('level')
        desc = get_param('content')

        # Create an instance and parse to the ExtractEngine
        if file:
            extractor = ExtractEngine(file)
            # Process the extracted text to generate a quiz (you can customize this as needed)
            quiz = quiz_result(extractor,level)
        else:
            quiz= quiz_result(desc[:25000],level)
        return JsonResponse(quiz, status=200)

    return JsonResponse({'error': 'No File or Content provided'}, status=400)

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
    dir = os.listdir(settings.MEDIA_ROOT)
    file_list= [file for file in dir if file not in ['cos.json','quiz']]
    ran_file= random.choice(file_list)
    extractor = ExtractEngine(os.path.join(settings.MEDIA_ROOT,ran_file))
    if level:
        quiz=quiz_result(extractor,level)
        return JsonResponse(quiz,status=200)
    quiz = quiz_result(extractor)
    return JsonResponse(quiz,status=200)

@csrf_exempt
def file_list(request):
    file_list = [file for file in os.listdir(settings.MEDIA_ROOT) if file not in ['quiz']]
    return JsonResponse({'Materials':file_list})


