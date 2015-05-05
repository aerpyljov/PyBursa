from django.shortcuts import render
from courses.models import Course
from courses.models import Lesson
from students.models import Student
from coaches.models import Coach


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')

def students(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(course=course_id)
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = student.course.all()
    return render(request, 'student_detail.html', {'student': student, 'courses': courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('item_no')
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})

def coach_detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    courses = coach.course.all()
    return render(request, 'coach_detail.html', {'coach': coach, 'courses': courses})
