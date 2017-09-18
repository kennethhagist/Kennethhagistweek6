# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.
def index(request):
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print get_random_string(length=14)

    return render(request, 'blogs/index.html', { "blogs": Blog.object.all() })
    #response = "placeholder to later display all the list of blogs"
    #return HttpResponse(response)

def new(request):
    return render(request, 'blogs/new.html')
    #response = "placeholder to display a new form to create a new blog"
    #return HttpResponse(response)

def show(request, blog_id):
    return render(request, 'blogs/show.html', { "blog": Blog.object.get(id = id) })
    #print blog_id
    #response = "placeholder to display blog {}".format(blog_id)
    #return HttpResponse(response)

def edit(request, blog_id):
    return render(request, 'blogs/edit.html', { "blog": Blog.object.get(id = id) })
    #response = "placeholder to edit blog {}".format(blog_id)
    #return HttpResponse(response)

def update(request, blog_id):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tag=tag)
        return redirect('/blogs/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST('name')
        blog.desc = request.POST('desc')
        blog.save()
        return redirect('/blogs')
    #return redirect(' ../show/'+id)

def destroy(request, blog_id):
    #insert code to delete/destory the specific resource
    return redirect('/blogs')

def delete(request, blog_id):
    return redirect('/blogs')

def create(request):
    #print request.method

    if request.method == "POST":
        print "*"*50
        print request.POST
        print reqeust.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

    #return redirect('/blogs')
