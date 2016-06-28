# -*- coding: utf-8 -*-
'''
Created on 2016-6-22

@author: WHX
'''
from django.conf.urls import url

import blog.views

handler404 = blog.views.page_not_found
handler500 = blog.views.page_error

urlpatterns = [
    url(r'^$',blog.views.welcome,name='welcome'),
    url(r'^about_me/$',blog.views.about_me,name='about_me'),
    url(r'^search/$',blog.views.blog_search, name = 'search'),
    url(r'^tag/(?P<tag>\w+)/$', blog.views.search_tag, name = 'search_tag'),
    url(r'^author/(?P<author>\w+)/$', blog.views.search_author, name = 'search_author'),
    url(r'^content/$',blog.views.article_list,name='content'),
    url(r'^article/(?P<id>\d+)/$',blog.views.article_detail,name='article_detail'),
]