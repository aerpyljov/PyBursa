from django.shortcuts import render

def pybursa (request):
    return render(request, 'index.html')

def pybursa_contact (request):
    return render(request, 'contact.html')


def pybursa_student_list (request):
    return render(request, 'student_list.html')


def pybursa_student_detail (request):
    return render(request, 'student_detail.html')
