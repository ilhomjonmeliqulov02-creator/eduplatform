from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('teacher', 'O\'qituvchi'),
        ('student', 'Talaba'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    university = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=100) # Kafedra
    specialty = models.CharField(max_length=100, blank=True, null=True) # Mutaxassislik
    diploma_file = models.FileField(upload_to='diplomas/')
    is_verified = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=100) # Yo'nalish
    course = models.PositiveIntegerField()
    student_id_card = models.FileField(upload_to='student_ids/')
    is_verified = models.BooleanField(default=False)