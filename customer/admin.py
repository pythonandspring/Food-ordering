from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'mother_name', 'student_class', 'phone_number',  'date_of_join')
    search_fields = ('first_name', 'last_name', 'father_name', 'mother_name', 'phone_number', 'class_teacher__first_name', 'class_teacher__last_name')
    list_filter = ('student_class',  'date_of_join')

admin.site.register(Student, StudentAdmin)
