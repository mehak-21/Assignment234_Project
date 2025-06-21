# Python
from django.urls import path, include

from . import views
from .views import (
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView,
    WorkExperienceDeleteView, WorkExperienceDetailView
)
# urls.py
from .views import select_template, download_resume_pdf

urlpatterns = [
    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),
    path('resume/download/', views.download_resume, name='download_resume'),
    path('resume/<int:resume_id>/select-template/', select_template, name='select_template'),
    path('resume/<int:resume_id>/download-pdf/', download_resume_pdf, name='download_resume_pdf'),
]