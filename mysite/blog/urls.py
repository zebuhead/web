__author__ = 'John Dees'

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>[0-9]+)', views.article, name='article'),
    url(r'^topic/(?P<topic_name>[a-z]+)', views.topic, name='topic'),
    url(r'^archive', views.archive, name='archive'),
]
