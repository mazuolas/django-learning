# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Models):
    question_text = models.CharField(max_lenght=200)
    pub_date = models.DateTimeField('date published')
