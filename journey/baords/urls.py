from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^baords/(?P<pk>\d+)/$', views.baords_topics, name='baords_topics'),
    #the line below displays another way in which you can configure your url patterns
    #re_path(r'^$', views.home, name='home'),


]