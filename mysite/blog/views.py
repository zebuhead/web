from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Blog

def index(request):
    blog_list = Blog.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
        'active': 'blog',
    })
    return HttpResponse(template.render(context))

def archive(request):
    blog_list = Blog.objects.order_by('-pub_date')
    template = loader.get_template('blog/archive.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
        'active': 'blog',
    })
    return HttpResponse(template.render(context))

def article(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    template = loader.get_template('blog/article.html')
    context = RequestContext(request, {
        'blog': blog,
        'active': 'blog',
    })
    return HttpResponse(template.render(context))

def topic(request, topic_name):
    blog_list = Blog.objects.filter(tags__contains=topic_name)
    in_list = 'True'
    if len(blog_list) == 0:
        in_list = 'False'
    template = loader.get_template('blog/topic.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
        'topic_name': topic_name,
        'in_list': in_list,
        'active': 'blog',
    })
    return HttpResponse(template.render(context))

