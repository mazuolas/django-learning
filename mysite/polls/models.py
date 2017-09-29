# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Models):
    question_text = models.CharField(max_lenght=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Models):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_lenght = 200)
    tally = models.IntgerField(default=0)
