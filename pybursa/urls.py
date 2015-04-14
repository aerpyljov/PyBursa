# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace = "polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),
    url(r'^$', views.show_index, name = 'index_itbursa'),
    url(r'^contact/$', views.show_contacts, name = 'contacts_itbursa'),
    url(r'^students/$', views.show_students, name = 'student_list'),
    url(r'^students/(?P<id>\d+)/$', views.show_student_detail, name = 'student_detail'),
    url(r'^courses/(?P<id>\d+)/$', views.show_courses, name = 'courses'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coaches/(?P<id_c>\d+)/$', views.show_coach_detail, name = 'coach_detail'),

)
