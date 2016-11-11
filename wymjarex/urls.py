from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.posts_list, name='posts_list'),
    url(r'^last/(?P<pk>[0-9]+)/$', views.last, name='last'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^accounts/login/$', TemplateView.as_view(template_name='wymjarex/login.html')),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='wymjarex/profile.html')),
]