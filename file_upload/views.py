from django.shortcuts import render, redirect
from .models import Assignment
from .open_edx_api import get_courses
from .forms import AssignmentForm
from django.http import JsonResponse

 
def api_get_files(request):
    files = Assignment.objects.values('id', 'course__course_id', 'student_id', 'file', 'uploaded_at')
    return JsonResponse(list(files), safe=False)

 
def list_courses(request):
    courses = get_courses()
    print(f"Courses: {courses}")  
    return render(request, 'file_upload/courses.html', {'courses': courses})

 
def upload_file(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload_success')
    else:
        form = AssignmentForm()
    return render(request, 'file_upload/upload.html', {'form': form})

 
def file_upload_success(request):
    return render(request, 'file_upload/success.html')

 
def list_files(request):
    files = Assignment.objects.all()
    return render(request, 'file_upload/files.html', {'files': files})
