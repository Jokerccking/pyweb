# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    string = u"Learn Django to WebPage"
    TutorialList = ['html','css','jQuery','Python','Django']
    info_dict = {'site': u'ZQXT', 'content': u'IT tech teaching',}
    return render(request, 'learn/home.html',{'string': string,'TutorialList': TutorialList,'info_dict': info_dict,})

# Create your views here.

def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
