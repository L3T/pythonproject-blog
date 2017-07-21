# coding=utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from articles.models import ArticlesV1
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse('Hello World, Django!')

def home_v2(request):
    post_list = ArticlesV1.objects.all()
    return render(request, 'home.html', {'post.html': post_list})
