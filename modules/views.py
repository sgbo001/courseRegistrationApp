from django.shortcuts import render
from .models import Course, Module, CourseModule

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
    
    
