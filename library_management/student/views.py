from django.shortcuts import render , redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    stud = Student.objects.all()
    return render(request, 'student/list.html', {'Student': stud})

@login_required()
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('stud_home')
    else:
        form = StudentForm()

    return render(request, 'student/add_student.html', {'form': form})
@login_required()
def edit_student(request,student_id):
    stud = Student.objects.get(pk=student_id)
    form = StudentForm(instance=stud)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('stud_home')
    return render(request, 'student/add_student.html', {'form': form})

@login_required()
def delete_student(request,student_id):
    stud = Student.objects.get(pk=student_id)
    stud.delete()
    return redirect('stud_home')

