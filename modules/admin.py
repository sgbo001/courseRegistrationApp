from django.contrib import admin
from .models import Course, Module, RegisteredUser, Learning


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(RegisteredUser)
admin.site.register(Learning)

admin.site.site_header = 'SHU App Admin'


