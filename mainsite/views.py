# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.shortcuts import redirect

reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except :
        return redirect('/')
        