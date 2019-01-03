# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.core import serializers
# Create your views here.

# Create your views here.
def mainpage(request):
    return HttpResponse('You shall not pass')

def cars_list(request):
    # page = request.GET['page']
    # c_list = Car.objects.all()
    # data = serializers.serialize("json", c_list)
    # return HttpResponse(data)
    # c_list = Car.objects.filter()       #<-- Car.objects.all() - pokazuje wszystkie obiekty w bazie
    # data = serializers.serialize("json", c_list)

    api = request.GET.get('api')
    if api == 'true':
        return HttpResponse(data)
    # else:
    #     return HttpResponse('Załaduj szablon')
    s = False       #<-- wyszukiwanie czy nie

    if request.GET.get('search'):
        s = True
        cm = request.GET.get('carmark')
        if not len(cm) > 3:
            err = 'Nie podałeś Modelu'
        cy = request.GET.get('caryear')
        if not cy:
            err = 'Nie podałeś rocznika'
        c_list = Car.objects.filter(mark__contains=cm)      #<-- dwa underscory!
    else:
        c_list = Car.objects.all()

    # if request.GET.get('search'):
    #     s = True
    #     # vars = []
    #     cm = request.GET.get('carmark')
    #     cy = request.GET.get('caryear')
    #     # if cm:
    #     #     vars['mark'] = cm
    #     # if cy:
    #     #     vars['year'] = cy
    #     c_list = Car.objects.filter(mark=cm, year=cy)       #<-- (vars)
    # else:
    #     c_list = Car.objects.all()

    tpl = loader.get_template('Rental/carslist.html')
    data = {
        'cars': c_list,
        'title': 'Lista samochodów',
        'search': s
    }
    ret = tpl.render(data)
    return HttpResponse(ret)

    # return HttpResponse(api)
    # return HttpResponse('Jesteś na stronie %s' %page)

    # autos = Car.objects.order_by('mark')
    # tpl = loader.get_template('Rental/carslist.html')
    # data = {
    #     'message': 'Orzeł wylądował',
    #     'fury': autos
    # }
    # return HttpResponse(tpl.render(data))

def car_item(request, car_id):
    car = Car.objects.get(pk=car_id)
    return HttpResponse('Chcesz podejrzeć autko o marce: %s' %car.mark)