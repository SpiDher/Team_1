from django.http import JsonResponse,HttpResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import ExtractEngine,text_content
from .ai.use_ai_gen_quiz import quiz_engine
import os
from Backend import settings
@csrf_exempt
def gen_quiz(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']
        level = request.POST.get('level', None)

        # Create an instance of the ExtractEngine
        extractor = ExtractEngine(file)

        # Process the extracted text to generate a quiz (you can customize this as needed)
        quiz = quiz_engine(extractor, level)

        return JsonResponse({'quiz': quiz}, status=200)

    return JsonResponse({'error': 'No file provided'}, status=400)

@csrf_exempt
def home(request):
    return HttpResponse('Welcome')

@csrf_exempt
def content(request):
    course_data = text_content()
    return JsonResponse({'course_data':course_data}, status=400)

@csrf_exempt
def topic_material(request):
    filename= request.GET.get('filename').lower()
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        file= open(file_path,'rb')
        try:
            response = FileResponse(file, as_attachment=True, filename=filename)
            return response
        except Exception as e:
            pass
    return JsonResponse({'error':'file not found'})




