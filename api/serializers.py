from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import PersonalInfo, Experience, Education, Project, Skill
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ['id', 'full_name', 'email', 'phone', 'location', 
                 'professional_title', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ExperienceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=False, allow_blank=True)
    company = serializers.CharField(max_length=100, required=False, allow_blank=True)
    duration = serializers.CharField(max_length=50, required=False, allow_blank=True)
    
    class Meta:
        model = Experience
        fields = ['id', 'title', 'company', 'location', 'duration', 
                 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class EducationSerializer(serializers.ModelSerializer):
    degree = serializers.CharField(max_length=100, required=False, allow_blank=True)
    institution = serializers.CharField(max_length=100, required=False, allow_blank=True)
    education_duration = serializers.CharField(max_length=50, required=False, allow_blank=True)
    
    class Meta:
        model = Education
        fields = ['id', 'degree', 'institution', 'education_duration', 
                 'education_location', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    duration = serializers.CharField(max_length=50, required=False, allow_blank=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'duration', 'description', 'technologies', 
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skills', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class APISchemaSerializer(serializers.Serializer):
    api_overview = serializers.CharField(read_only=True)
    complete_resume = serializers.CharField(read_only=True)
    personal_info = serializers.CharField(read_only=True)
    experience = serializers.CharField(read_only=True)
    education = serializers.CharField(read_only=True)
    projects = serializers.CharField(read_only=True)
    skills = serializers.CharField(read_only=True)


# Complete resume serializer for getting all user data at once
class CompleteResumeSerializer(serializers.Serializer):
    personal_info = PersonalInfoSerializer(read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(read_only=True)  # Remove many=True since it's OneToOneField
    progress = serializers.SerializerMethodField()

    @extend_schema_field({'type': 'object', 'properties': {
        'personalInfo': {'type': 'integer'},
        'experience': {'type': 'integer'},
        'education': {'type': 'integer'},
        'projects': {'type': 'integer'},
        'skills': {'type': 'integer'},
    }})
    def get_progress(self, obj):
        personal_info_progress = 0
        if obj['personal_info'] and obj['personal_info'].full_name:
            personal_info_progress = 100

        # Handle experiences
        experience_progress = 0
        if obj['experiences']:
            experience_progress = 100 if any(
                exp.title and exp.title.strip() and 
                exp.company and exp.company.strip() and 
                exp.location and exp.location.strip() and 
                exp.duration and exp.duration.strip() and 
                exp.description and exp.description.strip() 
                for exp in obj['experiences']
            ) else 0

        # Handle education
        education_progress = 0
        if obj['education']:
            education_progress = 100 if any(
                edu.degree and edu.degree.strip() and 
                edu.institution and edu.institution.strip() and 
                edu.education_duration and edu.education_duration.strip() and 
                edu.education_location and edu.education_location.strip() 
                for edu in obj['education']
            ) else 0

        # Handle projects
        projects_progress = 0
        if obj['projects']:
            projects_progress = 100 if any(
                proj.name and proj.name.strip() and 
                proj.duration and proj.duration.strip() and 
                proj.description and proj.description.strip() and 
                proj.technologies and proj.technologies.strip() 
                for proj in obj['projects']
            ) else 0

        # Handle skills - obj['skills'] is a single object, not a list
        skills_progress = 0
        if obj['skills'] and obj['skills'].skills and obj['skills'].skills.strip():
            skills_progress = 100

        return {
            'personalInfo': personal_info_progress,
            'experience': experience_progress,
            'education': education_progress,
            'projects': projects_progress,
            'skills': skills_progress
        }