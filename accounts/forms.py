from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class StudentRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="Ism")
    last_name = forms.CharField(max_length=50, label="Familiya")
    email = forms.EmailField(label="Email adresi", required=True)
    university = forms.CharField(max_length=100, label="Universitet")
    address = forms.CharField(max_length=255, label="Yashash joyi (Manzil)")
    department = forms.CharField(max_length=100, label="Yo'nalish")
    course = forms.IntegerField(label="Kurs")
    student_id_card = forms.FileField(label="Talaba guvohnomasi (ID Card / Pasport)")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'university')

class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="Ism")
    last_name = forms.CharField(max_length=50, label="Familiya")
    email = forms.EmailField(label="Email adresi", required=True)
    university = forms.CharField(max_length=100, label="Universitet")
    address = forms.CharField(max_length=255, label="Yashash joyi (Manzil)")
    department = forms.CharField(max_length=100, label="Kafedra")
    specialty = forms.CharField(max_length=100, label="Mutaxassislik")
    diploma_file = forms.FileField(label="Diplom nusxasi (PDF / Rasm)")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'university')