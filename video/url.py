
from django.conf.urls import url
from video import views

app_name = 'video'
urlpatterns = [
    url(r'^index-(?P<level_id>(\d+))-(?P<type_id>(\d+))-(?P<direction_id>(\d+)).html$', views.index),
]