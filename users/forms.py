from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from modules.models import Course
from .models import Student


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

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')
    secret_answer = forms.CharField(label='Secret Answer')
    password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        email = cleaned_data.get('email')
        secret_answer = cleaned_data.get('secret_answer')

        try:
            user = User.objects.get(email=email)
            profile = user.student
            if profile.secret_answer != secret_answer:
                raise forms.ValidationError("Invalid secret answer.")
            cleaned_data['user'] = user
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid email.")

        return cleaned_data
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image', 'date_of_birth', 'address', 'city', 'country', 'department', 'secret_question', 'secret_answer']