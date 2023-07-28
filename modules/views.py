from django.shortcuts import render, get_object_or_404
from .models import Course, Module, RegisteredUser
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'about.html')

def course_list(request):
    try:
        # Get all courses
        courses = Course.objects.all()
        
        # Create a list to store course information
        course_info = []
        
        # Iterate over the courses and extract the relevant information
        for course in courses:
            course_name = course.group.name
            course_image = course.image
            
            # Create a dictionary with the course information
            course_data = {
                'course_name': course_name,
                'course_image': course_image,
            }
            
            # Append the course data to the list
            course_info.append(course_data)
        
        # Pass the course information to the template
        return render(request, 'home.html', {'courses': course_info})
    
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
        filtered_modules = Module.objects.filter(module__code=course_code)

        # Create a list to store module information
        module_info = []

        # Iterate over the filtered modules and extract the relevant information
        for module in filtered_modules:
            course_name = module.course
            course_code = module.module.code
            credit = module.module.credit
            category = module.module.category
            available = module.module.available
            description = module.module.description

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


