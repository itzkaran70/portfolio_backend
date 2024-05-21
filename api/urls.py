from django.urls import path
from .views import (
    CertificateDetail,
    CertificateListCreate,
    ContactView,
    ProfileListCreate,
    ProfileDetail,
    ProjectListCreate,
    ProjectDetail,
    SkillListCreate,
    SkillDetail,
    ExperienceListCreate,
    ExperienceDetail,
    SocialMediaListCreate,
    SocialMediaDetail,
    get_title_strings,
)

urlpatterns = [
    path('profiles/', ProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('skills/', SkillListCreate.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetail.as_view(), name='skill-detail'),
    path('experiences/', ExperienceListCreate.as_view(), name='experience-list-create'),
    path('experiences/<int:pk>/', ExperienceDetail.as_view(), name='experience-detail'),
    path('social-media/', SocialMediaListCreate.as_view(), name='social-media-list-create'),
    path('social_media/<int:pk>/', SocialMediaDetail.as_view(), name='social-media-detail'),
    path('title-strings/', get_title_strings, name='get-typed-strings'),
    path('certificates/', CertificateListCreate.as_view(), name='certificate-list-create'),
    path('certificates/<int:pk>/', CertificateDetail.as_view(), name='certificate-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
