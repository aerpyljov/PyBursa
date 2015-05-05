#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from quadratic import check_coef, solve_quadratic_equation, get_discr


def results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    text = 'Кв ур a*x*x + b*x + c = 0\n'
    text += '\n• a = {0}'.format(a)
    text += check_coef(a, isA = True)
    text += '\n• b = {0}'.format(b)
    text += check_coef(b)
    text += '\n• c = {0}\n'.format(c)
    text += check_coef(c)
    if check_coef(a, isA = True) == '' and check_coef(b) == '' and check_coef(c) == '':
        text += '\nДискриминант: {0}\n\n'.format(get_discr(a, b, c))
        text += solve_quadratic_equation(a, b, c)
    return HttpResponse (text, content_type="text/plain; charset=utf-8")
