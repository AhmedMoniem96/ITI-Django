from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view

urlpatterns = [
    path('', home, name='home'),  
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),
    path('courses/', include('course.urls')),
]

