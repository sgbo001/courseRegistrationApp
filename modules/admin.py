from django.contrib import admin
from .models import Course, Module, RegisteredUser, CourseModule


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(RegisteredUser)
admin.site.register(CourseModule)


