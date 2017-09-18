# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def new(request):
    return redirect('/users')

def create(request):
    return redirect('/users')

def show(request, user_id):
    return HttpResponse("placeholder to display user {}".format(user_id))

def edit(request, user_id):
    return HttpResponse("placeholder to edit user {}".format(user_id))

def delete(request, user_id):
    return redirect('/users')
