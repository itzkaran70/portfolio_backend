from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Project, Skill, Experience, SocialMedia, TitleString, Certificate, Contact
from ckeditor.widgets import CKEditorWidget
from django.db import models

class ProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    list_display = ('name', 'image_thumbnail', 'resume', 'description_safe')

    def image_thumbnail(self, obj):
        if obj.imageSrc:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.imageSrc.url))
        return "-"
    image_thumbnail.short_description = 'Image'

    def description_safe(self, obj):
        return format_html(obj.description)
    description_safe.short_description = 'Description'

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    list_display = ('title', 'image_thumbnail', 'description_safe', 'link', 'source')

    def image_thumbnail(self, obj):
        if obj.imageSrc:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.imageSrc.url))
        return "-"
    image_thumbnail.short_description = 'Image'

    def description_safe(self, obj):
        return format_html(obj.description)
    description_safe.short_description = 'Description'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')

    def image_thumbnail(self, obj):
        if obj.imageSrc:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.imageSrc.url))
        return "-"
    image_thumbnail.short_description = 'Image'

class ExperienceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    list_display = ('role', 'organisation', 'startDate', 'endDate', 'location', 'image_thumbnail', 'experiences_safe')

    def image_thumbnail(self, obj):
        if obj.imageSrc:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.imageSrc.url))
        return "-"
    image_thumbnail.short_description = 'Image'

    def experiences_safe(self, obj):
        return format_html(obj.experiences)
    experiences_safe.short_description = 'Experiences'

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail', 'github_link', 'contact_no')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(TitleString)
admin.site.register(Certificate)
admin.site.register(Contact)