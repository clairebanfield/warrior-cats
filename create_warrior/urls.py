from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.catlist, name='catlist'),
    url(r'^cats/add/$', views.addcat, name='addcat'),
    url(r'^clans/add/$', views.addclan, name='addclan'),
    url(r'^cats/(?P<name>\D+)/edit/$', views.editcat, name='editcat'),
    url(r'^cats/(?P<name>\D+)/delete/$', views.deletecat, name='deletecat'),
    url(r'^cats/(?P<name>\D+)/$', views.catdetails, name='catdetails'),
	url(r'^clans/(?P<name>\D+)/delete/$', views.deleteclan, name='deleteclan'),
    url(r'^clans/(?P<name>\D+)/$', views.clandetails, name='clandetails'),
]

