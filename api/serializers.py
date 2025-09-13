from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import PersonalInfo, Experience, Education, Project, Skill


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
    skills = SkillSerializer(many=True, read_only=True)
    progress = serializers.SerializerMethodField()

    @extend_schema_field({'type': 'object', 'properties': {
        'personalInfo': {'type': 'integer'},
        'experience': {'type': 'integer'},
        'education': {'type': 'integer'},
        'projects': {'type': 'integer'},
        'skills': {'type': 'integer'},
    }})
    def get_progress(self, obj):
        return {
            'personalInfo': 100 if obj['personal_info'] else 0,
            'experience': 100 if obj['experiences'].exists() else 0,
            'education': 100 if obj['education'].exists() else 0,
            'projects': 100 if obj['projects'].exists() else 0,
            'skills': 100 if any(skill.skills.strip() for skill in obj['skills']) else 0
        }