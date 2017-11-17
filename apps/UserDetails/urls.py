from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name='my_index'),     # This line has changed!
    url(r'^(?P<id>\d+)$', views.show, name='my_show'),
    url(r'^(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^new$', views.new, name='my_new'),
    url(r'^create$', views.create, name='my_create'),
    url(r'^(?P<id>\d+)/delete$',views.delete, name='my_delete'),
    url(r'^(?P<id>\d+)/update$',views.update, name='my_update')
]