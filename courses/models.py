from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course)
    release_num = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title


