__author__ = 'John Dees'


from django.http import HttpResponse
from django.template import RequestContext, loader
from portfolio.models import Map
from blog.models import Blog


def home(request):
    map = Map.objects.get(pk=3)
    blog_list = Blog.objects.order_by('-pub_date')
    blog = blog_list[0]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'active': 'home',
        'map': map,
        'blog': blog,
    })
    return HttpResponse(template.render(context))

def cv(request):
    template = loader.get_template('CV.html')
    context = RequestContext(request, {
        'active': 'cv',
    })
    return HttpResponse(template.render(context))