# coding:utf-8

# compitable py2.xx and py3.xx
# from __future__ import unicode_literals
from django.db import models
# from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# @python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'title', max_length=256)
    content = models.TextField(u'content')

    pub_date = models.DateTimeField(u'ct', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'ut',auto_now=True, null=True)

    def __str__(self):
        return self.title

