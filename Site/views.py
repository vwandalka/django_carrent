# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader

# Create your views here.
def homepage(request):
    tpl = loader.get_template('Site/homepage.html')

    siteData = Page.objects.get(type='homepage')
    context = {
        'page': {
            'title': siteData.title,
            'content': siteData.content,
            'specials': siteData.get_extras()}
    }
    return HttpResponse(tpl.render(context))  # tpl jest obiektem, render zmienia go na kod HTML

def contact(request):
    tpl = loader.get_template('Site/contact.html')
    siteData = Page.objects.get(type='contact')
    context = {
        'page': {
            'title': siteData.title,
            'content': siteData.content,
            'specials': siteData.get_extras()}
    }
    return HttpResponse(tpl.render(context))
    # return HttpResponse('Kontakt')

def about(request):
    tpl = loader.get_template('Site/about.html')
    siteData = Page.objects.get(type='about')
    context = {
        'message': 'O nas',
        'menu': [
            'exp', 'more exp', 'link do gita', 'cokolwiek'
        ],
        'page': {
            'title': siteData.title,
            'content': siteData.content,
            'specials': siteData.get_extras()}
    }
    return HttpResponse(tpl.render(context))
    # return HttpResponse('O nas')

def header(request):
    tpl = loader.get_template('Site/header.html')
    siteData = Page.objects.get(type='header')
    context = {
        'page': {
            'title': siteData.title,
            'content': siteData.content,
            'specials': siteData.get_extras()}
    }
    return HttpResponse(tpl.render(context))
    # return HttpResponse('O nas')

def footer(request):
    tpl = loader.get_template('Site/footer.html')
    siteData = Page.objects.get(type='footer')
    context = {
        'page': {
            'title': siteData.title,
            'content': siteData.content,
            'specials': siteData.get_extras()}
    }
    return HttpResponse(tpl.render(context))
    # return HttpResponse('O nas')