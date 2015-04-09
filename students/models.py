# -*- coding: utf-8 -*-
from django.db import models

class Student(models.Model):
    name = models.CharField(u"Имя", max_length=255)
    surname = models.CharField(u"Фамилия", max_length=255)
    date_of_birth = models.DateField(u"Дата рождения")
    email = models.EmailField(u"Эл. почта")
    phone = models.CharField(u"Телефон", max_length=255)
    address = models.CharField(u"Адрес", max_length=255)
    skype = models.CharField(u"Скайп", max_length=255)
    courses = models.ManyToManyField('courses.Course', verbose_name=u"Курсы")

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)

    def courseset(self):
        return self.courses.all()