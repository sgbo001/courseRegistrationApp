
from django.contrib import admin
from django.urls import path
from modules import views
from users.views import register
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about, name = 'about'),
    path('register/', views.register, name='register'),
    path('login', auth_views.LogoutView.as_view(template_name = 'login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('profile', user_views.profile, name = 'profile'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


