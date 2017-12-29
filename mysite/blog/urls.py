from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<artical_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<artical_id>\d+)/(?P<obj_type>\w+)/(?P<auor>\w+)/$', views.favorite, name='favorite'),
]