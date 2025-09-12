from django.urls import path
from . import views

urlpatterns = [
    # API Overview
    path('', views.api_overview, name='api-overview'),
    
    # Complete Resume
    path('resume/', views.complete_resume, name='complete-resume'),
    
    # Personal Info
    path('personalInfo/', views.PersonalInfoView.as_view(), name='personal-info'),
    
    # Experience
    path('experience/', views.ExperienceListCreateView.as_view(), name='experience-list'),
    path('experience/<int:pk>/', views.ExperienceDetailView.as_view(), name='experience-detail'),
    
    # Education
    path('education/', views.EducationListCreateView.as_view(), name='education-list'),
    path('education/<int:pk>/', views.EducationDetailView.as_view(), name='education-detail'),
    
    # Projects
    path('projects/', views.ProjectListCreateView.as_view(), name='projects-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='projects-detail'),
    
    # Skills
    path('skills/', views.SkillView.as_view(), name='skills'),
]