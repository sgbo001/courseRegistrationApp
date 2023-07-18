from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = 'profile_pics/default.png', upload_to = 'profile_pics')
    date_of_birth = models.CharField(default = '', max_length=100, blank=True)
    address = models.CharField(default = '', max_length=100, blank=True)
    city = models.CharField(default = '', max_length=50, blank=True)
    country = models.CharField(default = '', max_length=50, blank=True)
    secret_question = models.CharField(default='', max_length=100, blank=True, choices=(
        ("maiden_name", "Your mom's maiden name"),
        ("best_color", "Your best color"),
        ("football_team", "Your favorite football team"),
    ))
    secret_answer = models.CharField(default = '', max_length=50, blank=True)
    department = models.CharField(default = '', max_length=50, blank=True)
    
def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
