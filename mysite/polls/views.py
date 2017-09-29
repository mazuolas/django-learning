# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)
