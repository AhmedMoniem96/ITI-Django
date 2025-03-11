from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def trainee_add(request):
    if request.method == 'POST':
        print("✅ Form submitted!")  # Check if request reaches here
        print("POST Data:", request.POST)  # See what data is sent

        form = TraineeForm(request.POST)
        if form.is_valid():
            print("✅ Form is valid!")  # Check if validation passes
            form.save()
            return redirect('trainee_list')
        else:
            print("❌ Form errors:", form.errors)  # Check for validation errors
    else:
        form = TraineeForm()
    
    return render(request, 'trainee/add.html', {'form': form})

def trainee_update(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/update.html', {'form': form})

def trainee_delete(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    trainee.delete()
    return redirect('trainee_list')
