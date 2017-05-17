from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^list1/$', views.post_list1),
]
