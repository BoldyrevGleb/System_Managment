from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import TeacherRegistrationForm
from .models import Teacher

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def teacher_management(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Teacher.objects.create(
                user=user,
                department=form.cleaned_data['department'],
                position=form.cleaned_data['position'],
                phone=form.cleaned_data['phone']
            )
            messages.success(request, 'Преподаватель успешно зарегистрирован')
            return redirect('teachers:teacher_management')
    else:
        form = TeacherRegistrationForm()
    
    teachers = Teacher.objects.all()
    return render(request, 'teachers/management.html', {
        'form': form,
        'teachers': teachers
    })

@user_passes_test(is_superuser)
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers}) 