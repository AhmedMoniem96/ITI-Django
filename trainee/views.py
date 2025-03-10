from django.shortcuts import render
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})
