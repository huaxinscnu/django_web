#coding:utf-8
'''
Created on 2016-5-31

@author: WHX
'''
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from UserManage.forms import RoleListForm
from UserManage.models import RoleList
from UserManage.views.permission import PermissionVerify
from mydjango.common.CommonPaginator import SelfPaginator


@login_required
@PermissionVerify()
def AddRole(request):
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('UserManage/role.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListRole(request):
    mList = RoleList.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('UserManage/role.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditRole(request,ID):
    iRole = RoleList.objects.get(id=ID)

    if request.method == "POST":
        form = RoleListForm(request.POST,instance=iRole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm(instance=iRole)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('UserManage/role.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteRole(request,ID):
    RoleList.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listroleurl'))
