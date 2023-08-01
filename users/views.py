from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Student, User
from .forms import UserRegisterForm, UserProfileForm, PasswordResetForm, ProfileEditForm
from django import forms


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
            profile.department = selected_department if selected_department else None
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


def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            secret_answer = form.cleaned_data['secret_answer']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                profile = user.student
                if profile.secret_answer != secret_answer:
                    raise forms.ValidationError("Invalid secret answer.")
                user.set_password(password)  # Set a new password here
                user.save()
                messages.success(request, f'Your account has been reset successfully!')
                return redirect('login')  # Redirect to the login page after successful password reset
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid email.")
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def edit_profile(request):
    profile = request.user.student

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')  # Redirect to the updated profile page
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})