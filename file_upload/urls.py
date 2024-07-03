from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.file_upload_success, name='file_upload_success'),
    path('files/', views.list_files, name='list_files'),
    path('courses/', views.list_courses, name='list_courses'),
    
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
