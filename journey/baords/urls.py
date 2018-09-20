from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^baords/(?P<pk>\d+)/$', views.baords_topics, name='baords_topics'),
    re_path(r'^baords/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    #the line below displays another way in which you can configure your url patterns



]