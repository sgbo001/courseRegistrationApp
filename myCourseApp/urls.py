
from django.contrib import admin
from django.urls import path
from modules import views
from users.views import register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about, name = 'about'),
    path('register/', views.register, name='register')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
