from django.urls import path, include
from rest_framework.routers import DefaultRouter

from resume_builder.api.api import (
    ResumeTemplateViewSet, ResumeViewSet, ResumeSectionViewSet,
    WorkExperienceViewSet, TechnicalSkillViewSet, EducationViewSet,
    TechnologyViewSet, ProjectViewSet, CertificationViewSet,
    AwardViewSet, LanguageViewSet
)

from . import views

# DRF Router setup
router = DefaultRouter()
router.register(r'resume-templates', ResumeTemplateViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'resume-sections', ResumeSectionViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'technical-skills', TechnicalSkillViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    # REST API endpoints
    path('api/', include(router.urls)),

    # Allauth user authentication
    path('accounts/', include('allauth.urls')),

    # Work Experience CRUD
    path('workexperience/', views.workexperience_list, name='workexperience_list'),
    path('workexperience/create/', views.create_workexperience, name='create_workexperience'),
    path('workexperience/<int:pk>/', views.workexperience_detail, name='workexperience_detail'),
    path('workexperience/<int:pk>/edit/', views.update_workexperience, name='update_workexperience'),
    path('workexperience/<int:pk>/delete/', views.delete_workexperience, name='delete_workexperience'),
]
