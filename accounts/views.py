from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkExperience
from .forms import WorkExperienceForm
from django.contrib.auth.decorators import login_required

@login_required
def workexperience_list(request):
    records = WorkExperience.objects.filter(user=request.user)
    return render(request, 'resume_builder/workexperience_list.html', {'records': records})

@login_required
def workexperience_add(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('workexperience_list')
    else:
        form = WorkExperienceForm()
    return render(request, 'resume_builder/workexperience_form.html', {'form': form})

@login_required
def workexperience_edit(request, pk):
    exp = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    form = WorkExperienceForm(request.POST or None, instance=exp)
    if form.is_valid():
        form.save()
        return redirect('workexperience_list')
    return render(request, 'resume_builder/workexperience_form.html', {'form': form})

@login_required
def workexperience_delete(request, pk):
    exp = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        exp.delete()
        return redirect('workexperience_list')
    return render(request, 'resume_builder/workexperience_confirm_delete.html', {'object': exp})