from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.wpiss_list, name='wpiss_list'),
    url(r'^last/(?P<pk>[0-9]+)/$', views.last, name='last'),
    url(r'^wpis/new/$', views.wpis_new, name='wpis_new'),
    url(r'^wpis/(?P<pk>[0-9]+)/edit/$', views.wpis_edit, name='wpis_edit'),
	url(r'^accounts/login/$', TemplateView.as_view(template_name='wymjarex/login.html')),
	url(r'^accounts/profile/', TemplateView.as_view(template_name='wymjarex/profile.html')),
]