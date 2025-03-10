from django.urls import path
from .views import trainee_list

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
]
