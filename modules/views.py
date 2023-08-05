from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Module, RegisteredUser, Learning
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.paginator import Paginator

def about(request):
    return render(request, 'about.html')

def course_list(request):
    try:
        # Get all courses
        courses = Course.objects.all()
        
        # Paginate the courses
        items_per_page = 6
        paginator = Paginator(courses, items_per_page)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Pass the paginated courses to the template
        return render(request, 'home.html', {'page_obj': page_obj})
    
    except Course.DoesNotExist:
        # Handle error case if no courses are found
        return render(request, 'error.html', {'message': 'No courses found'})

def module_list(request):
    course_name = request.GET.get('course_name')

    try:
        # Filter the modules based on the provided course_name
        filtered_modules = Module.objects.filter(courses__group__name=course_name)

        # Create a list to store module information
        module_info = []

        # Iterate over the filtered modules and extract the relevant information
        for module in filtered_modules:
            course_name = module.name
            course_code = module.code
            credit = module.credit
            category = module.category
            available = module.available
            description = module.description
            #course_title = module.name.name.all()

            # Create a dictionary with the module information
            module_data = {
                'course_name': course_name,
                'course_code': course_code,
                'credit': credit,
                'category': category,
                'available': available,
                'description': description,
                #'course_title': course_title
            }

            # Append the module data to the list
            module_info.append(module_data)

        # Pass the module information to the template
        return render(request, 'module_list.html', {'modules': module_info})
    except Module.DoesNotExist:
        # Handle error case if no modules are found
        return render(request, 'error.html', {'message': 'No modules found'})
    
@login_required
def module_detail(request):
    course_code = request.GET.get('course_code')

    try:
        # Filter the modules based on the provided course_code
        filtered_modules = Module.objects.filter(code=course_code)

        # Create a list to store module information
        module_info = []

        # Iterate over the filtered modules and extract the relevant information
        for module in filtered_modules:
            course_name = module.name
            course_code = module.code
            credit = module.credit
            category = module.category
            available = module.available
            description = module.description

            # Create a dictionary with the module information
            module_data = {
                'course_name': course_name,
                'course_code': course_code,
                'credit': credit,
                'category': category,
                'available': available,
                'description': description,
            }

            # Append the module data to the list
            module_info.append(module_data)

        # Filter the registered users based on the provided course_code
        registered_users = RegisteredUser.objects.filter(module_code__code=course_code)

        # Create a list to store user information
        user_info = []

        # Iterate over the filtered users and extract the relevant information
        for registered_user in registered_users:
            student = registered_user.student
            registration_date = registered_user.registration_date

            # Create a dictionary with the user information
            user_data = {
                'student': student,
                'registration_date': registration_date,
            }

            # Append the user data to the list
            user_info.append(user_data)

        # Check if the user is a registered student for the module
        is_registered = RegisteredUser.objects.filter(student=request.user, module_code__code=course_code).exists()

        # Pass the module and user information to the template
        context = {
            'modules': module_info,
            'users': user_info,
            'is_registered': is_registered,
        }
        return render(request, 'module_detail.html', context)

    except Module.DoesNotExist:
        # Handle error case if no modules are found
        return render(request, 'error.html', {'message': 'No modules found'})
    except RegisteredUser.DoesNotExist:
        # Handle error case if no users are found
        return render(request, 'error.html', {'message': 'No users found'})


@login_required
def register_module(request, module_code):
    # Get the user and module based on the current user and module code
    user = request.user
    course_name = request.GET.get('course_name')
    try:
        # Get the module based on the module_code and course_name
        module = get_object_or_404(Module, code=module_code)
        course = get_object_or_404(Course, group__name=course_name)
        
        # Create a new Module object and save it to the database
        course_module = Module(name=course, code=module)
        
        
        # Create a new RegisteredUser object and save it to the database
        registered_user = RegisteredUser(student=user, module_code=course_module.code)
        registered_user.save()
        
        # Redirect to the module detail page or any other desired page
        messages.success(request, f'You have registered for this module successfully')
        return redirect('modules:my_module')  # Replace 'my_module' with the appropriate URL name

    except (Module.DoesNotExist, Course.DoesNotExist):
        # Handle the case when the module or course does not exist
        return render(request, 'module_not_found.html')
    
@login_required
def unregister_module(request, module_code):
    # Get the user and module based on the current user and module code
    user = request.user
    course_code = request.GET.get('course_code')
    try:
        # Get the registered user for the module
        registered_user = RegisteredUser.objects.get(student=user, module_code__code=course_code)
        
        # Delete the registered user
        registered_user.delete()
        messages.warning(request, f'You have un-registered from this module')
        # Redirect to the module detail page or any other desired page
        return redirect('modules:my_module')  # Replace 'my_module' with the appropriate URL name

    except (Module.DoesNotExist, RegisteredUser.DoesNotExist):
        # Handle the case when the module or registered user does not exist
        return render(request, 'module_not_found.html')

def my_module(request):
    student_name = request.user  # Replace with the actual student name

    # Query the RegisteredUser model to filter by student name
    registered_users = RegisteredUser.objects.filter(student__username=student_name)

    # Query the Module model to retrieve the corresponding module information
    modules = Module.objects.filter(pk__in=registered_users.values_list('module_code', flat=True))

    return render(request, 'myModule.html', {'modules': modules})

def learning_list(request):
    course_code = request.GET.get('course_code')

    try:
        # Filter the learnings based on the provided course_code
        filtered_learnings = Learning.objects.filter(module__code=course_code)

        # Create a list to store learning information
        learning_info = []

        # Iterate over the filtered learnings and extract the relevant information
        for learning in filtered_learnings:
            title = learning.title
            files = learning.files
            description = learning.description

            # Create a dictionary with the learning information
            learning_data = {
                'title': title,
                'files': files,
                'description': description,
            }

            # Append the learning data to the list
            learning_info.append(learning_data)

        # Pass the learning information to the template
        return render(request, 'learning_list.html', {'learnings': learning_info})
    except Learning.DoesNotExist:
        # Handle error case if no learnings are found
        return render(request, 'error.html', {'message': 'No learning material found'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose the email message
            email_subject = f"Contact Form Submission - {subject}"
            email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email using Django's send_mail function
            send_mail(
                email_subject,
                email_body,
                'sample@gmail.com',  # Replace this with your own email address
                ['sample@gmail.com'],  # Add your Gmail account here
                fail_silently=False,
            )

            messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
            return redirect('./')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
