from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegisterForm, TeacherRegisterForm
from .models import StudentProfile, TeacherProfile

def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.role = 'student'
            user.save()
            StudentProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                department=form.cleaned_data['department'],
                course=form.cleaned_data['course'],
                student_id_card=form.cleaned_data['student_id_card']
            )
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'role_title': 'Talaba'})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.role = 'teacher'
            user.save()
            TeacherProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                department=form.cleaned_data['department'],
                specialty=form.cleaned_data['specialty'],
                diploma_file=form.cleaned_data['diploma_file']
            )
            login(request, user)
            return redirect('home')
    else:
        form = TeacherRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'role_title': 'O\'qituvchi'})