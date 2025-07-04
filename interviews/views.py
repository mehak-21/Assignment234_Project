from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from resume_builder.models import WorkExperience
from resume_builder.forms import WorkExperienceForm

@login_required
def create_workexperience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('workexperience_list')
    else:
        form = WorkExperienceForm()
    return render(request, 'resume_builder/workexperience_form.html', {'form': form})

@login_required
def workexperience_list(request):
    items = WorkExperience.objects.filter(user=request.user)
    return render(request, 'resume_builder/workexperience_list.html', {'items': items})

@login_required
def workexperience_detail(request, pk):
    item = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    return render(request, 'resume_builder/workexperience_detail.html', {'item': item})

@login_required
def update_workexperience(request, pk):
    item = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('workexperience_list')
    else:
        form = WorkExperienceForm(instance=item)
    return render(request, 'resume_builder/workexperience_form.html', {'form': form})

@login_required
def delete_workexperience(request, pk):
    item = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('workexperience_list')
    return render(request, 'resume_builder/workexperience_confirm_delete.html', {'item': item})
