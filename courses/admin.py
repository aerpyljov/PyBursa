from django.contrib import admin
from courses.models import Course, Lesson
from coaches.models import Coach

admin.site.register(Lesson)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    #model = Lesson
    #filter_vertical = ('descr',)
    search_fields = ['title']
    list_display = [ 'title', 'descr']
    inlines = [LessonInline]


#    list_editable = ['title']
admin.site.register(Course, CourseAdmin)
