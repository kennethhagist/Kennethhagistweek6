# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M %p")
        #"Time":strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'display/page.html', context)
