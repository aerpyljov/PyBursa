from django.contrib import admin
from students.models import Student, CourseApplication

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone']
    list_per_page = 5
    ordering = ['surname', 'name']

admin.site.register(Student, StudentAdmin)
admin.site.register(CourseApplication)


