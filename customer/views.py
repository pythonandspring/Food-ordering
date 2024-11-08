from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'home/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'home/student_detail.html', {'student': student})
