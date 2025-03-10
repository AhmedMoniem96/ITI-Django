from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),  
    path('courses/', include('course.urls')), 
]
