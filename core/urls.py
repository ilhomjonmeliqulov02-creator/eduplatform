from django.contrib import admin
from django.urls import path, include
from courses.views import home
from accounts.views import register_student, register_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/student/', register_student, name='register_student'),
    path('register/teacher/', register_teacher, name='register_teacher'),
    path('accounts/', include('django.contrib.auth.urls')),
]