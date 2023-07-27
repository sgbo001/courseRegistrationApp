from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from modules.models import Course


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class DepartmentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, course):
        return course.group.name
    
class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'], help_text='YYYY-mm-dd')
    department = DepartmentChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = ['image', 'date_of_birth', 'address', 'city', 'country', 'department', 'secret_question', 'secret_answer']
