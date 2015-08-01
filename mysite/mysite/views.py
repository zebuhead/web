__author__ = 'John Dees'


from django.http import HttpResponse
from django.template import RequestContext, loader


def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'active': 'home',
    })
    return HttpResponse(template.render(context))

def cv(request):
    template = loader.get_template('CV.html')
    context = RequestContext(request, {
        'active': 'cv',
    })
    return HttpResponse(template.render(context))