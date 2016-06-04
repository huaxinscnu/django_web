#coding:utf-8
'''
Created on 2016-5-31

@author: WHX
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext


@login_required
def Home(request):
    return render_to_response('home.html',locals(),RequestContext(request))

def About(request):
    return render_to_response('about.html',locals(),RequestContext(request))
