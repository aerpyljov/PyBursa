from django.db import models
from coaches.models import Coach
# Create your models here.


class Course (models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    info = models.CharField(verbose_name='Short discription',null=True, blank=True, max_length=200)
    discription = models.TextField(verbose_name='Course discription', null=True, blank=True)
    teacher = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
    assistent = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name


class Lesson (models.Model):
    theme = models.CharField(verbose_name='Theme of lesson', max_length=40)
    discription = models.TextField(verbose_name='Lesson discription', null=True, blank=True)
    course = models.ForeignKey(Course)
    number = models.PositiveIntegerField(verbose_name='Number of lesson')

    def __unicode__(self):
        return str(self.number) + ' ' + self.theme
