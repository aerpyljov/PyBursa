from django.db import models
import courses
from django.core.urlresolvers import reverse

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(courses.models.Course)
	
    def full_name(self):
        return self.name + ' ' + self.surname

    
    def __unicode__(self):
        return self.surname


   # def get_absolute_url(self):
    #    return reverse("students:get_student", pk=self.pk)


