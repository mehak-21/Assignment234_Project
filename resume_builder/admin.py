from django.contrib import admin
from .models import WorkExperience, Education, Project, Certification, Award, Language, TechnicalSkill

# Register all models to appear in admin panel
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Award)
admin.site.register(Language)
admin.site.register(TechnicalSkill)
