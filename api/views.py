from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import PersonalInfo, Experience, Education, Project, Skill
from .serializers import (
    PersonalInfoSerializer, ExperienceSerializer, EducationSerializer,
    ProjectSerializer, SkillSerializer, CompleteResumeSerializer, APISchemaSerializer, UserRegistrationSerializer
)


@extend_schema(responses={200: APISchemaSerializer})
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
        'Register': '/api/register/',
        'Login': '/api/login/',
    }
    serializer = APISchemaSerializer(instance=api_urls)
    return Response(serializer.data)


@extend_schema(responses={200: CompleteResumeSerializer})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def complete_resume(request):
    """
    Get complete resume data
    """
    data = {
        'personal_info': PersonalInfo.objects.filter(user=request.user).first(),
        'experiences': Experience.objects.filter(user=request.user),
        'education': Education.objects.filter(user=request.user),
        'projects': Project.objects.filter(user=request.user),
        'skills': Skill.objects.filter(user=request.user).first()
    }
    
    serializer = CompleteResumeSerializer(instance=data)
    return Response(serializer.data)


# Personal Info Views
class PersonalInfoView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        personal_info, created = PersonalInfo.objects.get_or_create(
            user=user,
            defaults={
                'full_name': '',
                'email': '',
                'phone': '',
                'location': '',
                'professional_title': ''
            }
        )
        return personal_info

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Experience Views
class ExperienceListCreateView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


# Education Views
class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


# Skill Views
class SkillView(generics.RetrieveUpdateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        skill, created = Skill.objects.get_or_create(
            user=self.request.user,
            defaults={
                'skills': ''
            }
        )
        return skill

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
