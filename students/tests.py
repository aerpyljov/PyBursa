# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from students.models import Student
from courses.models import Course
from datetime import date
from django.core.urlresolvers import reverse


class StudentsTests(TestCase):

    # тест списка студентов
    def test_students_list(self):
        # запуск проекта
        client = Client()
        # переходим на страницу списка студентов
        response = client.get('/students/')
        # проверка что страничка работает
        self.assertEqual(response.status_code, 200)
        # проверка что список пока пуст (в б.д. ноль студентов)
        self.assertEqual(Student.objects.all().count(), 0)
        #self.assertNotContains(response, u'Булгаков')
        # создадим студента
        student1 = Student.objects.create(name=u'Миша', surname=u'Булгаков', date_of_birth=date(1891, 05, 03),
                                          email='master@margarita.com', phone='321', address=u'Киев-Москва',
                                          skype='Misha')
        # проверим что студент появился в списке
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Миша')
        self.assertEqual(Student.objects.all().count(), 1)

    # тест информации про студента
    def test_students_detail(self):
        client = Client()
        response = client.get('/students/1/')
        # проверка что страницы не существует
        self.assertEqual(response.status_code, 404)
        # создание курса
        course1 = Course.objects.create(name='Python/Django', short_description="Wed development with Django")
        # создание студента
        student1 = Student.objects.create(name=u'Миша', surname=u'Булгаков', date_of_birth=date(1891, 05, 03),
                                          email='master@margarita.com', phone='321', address=u'Киев-Москва',
                                          skype='Misha')
        student1.courses.add(course1)
        #response = client.get('/students/1/')
        response = client.get(reverse('students:student_info', args=(course1.id,)))
        # проверка странички
        self.assertEqual(response.status_code, 200)
        # проверка наличия информации о сдуденте на стриничке
        self.assertContains(response, u'Миша Булгаков')
        # провека количества студентов в б.д.
        self.assertEqual(Student.objects.all().count(), 1)
