from django.db import models
from django.contrib.auth.models import Group


class Course(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, blank=True)
    image = models.ImageField(default='course_pics/logo.jpg', upload_to='course_pics')
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.group.name
