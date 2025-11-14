from django.contrib import admin
from .models import (
    AboutMe,
    Skills,
    ProfessionalSkills,
    Education,
    Contact
)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_name', 'email', 'phone_number', 'location')
    search_fields = ('name', 'job_name', 'email')
    list_filter = ('location',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'percentage')
    list_filter = ('percentage',)
    search_fields = ('title',)


@admin.register(ProfessionalSkills)
class ProfessionalSkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'percentage')
    list_filter = ('percentage',)
    search_fields = ('title',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year')
    search_fields = ('title', 'year')
    list_filter = ('year',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
