from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Map, Project, Publication

def home(request):
    template = loader.get_template('portfolio/home.html')
    context = RequestContext(request, {
        'active': 'home',
    })
    return HttpResponse(template.render(context))

def index(request):
    maps_list = Map.objects.order_by('-pub_date')
    pubs_list = Publication.objects.order_by('-pub_date')
    template = loader.get_template('portfolio/index.html')
    context = RequestContext(request, {
        'maps_list': maps_list,
        'pubs_list': pubs_list,
        'active': 'portfolio',
    })

    return HttpResponse(template.render(context))



def detail(request, map_id):
    map = Map.objects.get(pk=map_id)
    map_image = map.image
    template = loader.get_template('portfolio/map.html')
    context = RequestContext(request, {
        'map': map,
        'active': 'portfolio',
    })
    return HttpResponse(template.render(context))



