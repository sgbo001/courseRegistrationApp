from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Student
from .forms import UserRegisterForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        username = form.data['username']
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            # Check if a profile already exists for the user
            profile, created = Student.objects.get_or_create(user=user)
            
            # Update the profile fields
            profile.image = profile_form.cleaned_data['image']
            profile.date_of_birth = datetime.fromisoformat(str(profile_form.cleaned_data['date_of_birth']))
            profile.address = profile_form.cleaned_data['address']
            profile.city = profile_form.cleaned_data['city']
            profile.country = profile_form.cleaned_data['country']
            profile.secret_question = profile_form.cleaned_data['secret_question']
            profile.secret_answer = profile_form.cleaned_data['secret_answer']
            
            # Save the department name
            selected_department = profile_form.cleaned_data['department']
            profile.department = selected_department.name if selected_department else ''
            profile.save()
            
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, f'Unable to create an account for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
        return render(request, 'register.html', {'form': form, 'profile_form': profile_form, 'title': 'Student Registration'})


@login_required
def profile(request):
    user = request.user
    profile = user.student
    context = {'user': user, 'profile': profile}
    return render(request, 'profile.html', context)