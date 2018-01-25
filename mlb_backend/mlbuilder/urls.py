from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mlmodel_list),
    url(r'^(?P<pk>[0-9]+)/$', views.mlmodel_detail),
]