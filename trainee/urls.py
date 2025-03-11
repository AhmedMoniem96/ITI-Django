from django.urls import path
from .views import trainee_list, trainee_add, trainee_update, trainee_delete  

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('add/', trainee_add, name='trainee_add'),
    path('update/<int:pk>/', trainee_update, name='trainee_update'),
    path('delete/<int:pk>/', trainee_delete, name='trainee_delete'),  
]
