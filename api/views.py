from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import PersonalInfo, Experience, Education, Project, Skill
from .serializers import (
    PersonalInfoSerializer, ExperienceSerializer, EducationSerializer,
    ProjectSerializer, SkillSerializer, CompleteResumeSerializer
)


@api_view(['GET'])
def api_overview(request):
    """
    API Overview - Lists available endpoints
    """
    api_urls = {
        'API Overview': '/api/',
        'Complete Resume': '/api/resume/',
        'Personal Info': '/api/personalInfo/',
        'Experience': '/api/experience/',
        'Education': '/api/education/',
        'Projects': '/api/projects/',
        'Skills': '/api/skills/',
    }
    return Response(api_urls)


@api_view(['GET'])
def complete_resume(request):
    """
    Get complete resume data
    """
    data = {
        'personal_info': PersonalInfo.objects.first(),
        'experiences': Experience.objects.all(),
        'education': Education.objects.all(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all()
    }
    
    serializer = CompleteResumeSerializer(data)
    return Response(serializer.data)


# Personal Info Views
class PersonalInfoView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonalInfoSerializer
    
    def get_object(self):
        personal_info, created = PersonalInfo.objects.get_or_create(
            defaults={
                'full_name': '',
                'email': '',
                'phone': '',
                'location': '',
                'professional_title': ''
            }
        )
        return personal_info


# Experience Views
class ExperienceListCreateView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


# Education Views
class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


# Skill Views
class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
