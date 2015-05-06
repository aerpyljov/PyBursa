# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from students.forms import StudentForm

import logging
logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id:
            queryset = queryset.filter(course__id=int(course_id))
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super(StudentListView, self).get_context_data(**kwargs)
        page_path = '?'
        course_id = self.request.GET.get('course_id')
        if course_id:
            page_path = '?course_id={0}&'.format(course_id)
        context_data['page_path'] = page_path
        # import pdb; pdb.set_trace()
        return context_data


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        logger.debug("Show DetailView Student debug")
        logger.info("Show DetailView Student info")
        logger.error("Show DetailView Student error")
        logger.warning("Show DetailView Student warning")
        return super(StudentDetailView, self).get_context_data(**kwargs)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Создать студента'
        context_data['h3_title'] = 'Создание нового студента'
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, u'Студент {0} успешно добавлен'.format(self.object.full_name()))
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Редактирование студента'
        context_data['h3_title'] = 'Редактирование данных студента'
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные студента {0} успешно изменены'.format(self.object.full_name()))
        return response


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:index')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Студент {0} успешно удален'.format(self.object.full_name()))
        return response

