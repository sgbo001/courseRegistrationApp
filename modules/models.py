from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Course, Module

class Course(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, blank=True)
    image = models.ImageField(default='course_pics/logo.jpg', upload_to='course_pics')
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.group.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credit = models.CharField(max_length=10)
    category = models.CharField(max_length=250, choices=(
        ("Compulsory", "Compulsory"),
        ("Elective", "Elective"),
    ))
    description = models.TextField()
    available = models.BooleanField()
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name
    
class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.module}"
    
class RegisteredUser(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE) 
    registration_date = models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        return f"{self.student} - {self.module_code}"