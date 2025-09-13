from django.db import models


class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    professional_title = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Experience(models.Model):
    title = models.CharField(max_length=100, blank=True)  # job title
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=50, blank=True)  # e.g., "01/2020 - 12/2022"
    description = models.TextField(blank=True)  # bullet points
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    education_duration = models.CharField(max_length=50, blank=True)  # e.g., "09/2018 - 05/2022"
    education_location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Project(models.Model):
    name = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=50, blank=True)  # e.g., "03/2023 - 05/2023"
    description = models.TextField(blank=True)  # bullet points
    technologies = models.TextField(blank=True)  # comma-separated technologies
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Skill(models.Model):
    skills = models.TextField(blank=True)  # comma-separated skills string
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return "Skills"
