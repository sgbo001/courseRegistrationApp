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
        print(profile_form.errors)
        username = form.data['username']
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            # ... (rest of the code for successful account creation)
            
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            # Collect all form errors into a string
            all_errors = "\n".join(
                [f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()]
                + [f"{field}: {', '.join(errors)}" for field, errors in profile_form.errors.items()]
            )
            
            # Include the form errors in the error message
            error_message = f"Unable to create an account:\n{all_errors}"
            messages.warning(request, error_message)
            return redirect('register')
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