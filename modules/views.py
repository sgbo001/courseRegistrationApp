from django.shortcuts import render
from .models import Course

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
