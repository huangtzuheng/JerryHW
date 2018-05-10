from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.post_page, name='new'),
    url(r'^edit/$', views.edit_page, name='edit'),
    url(r'^save/$', views.save, name='save'),
    #url(r'^delete/$', views.delete, name='delete'),
]