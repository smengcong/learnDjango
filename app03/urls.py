
from django.conf.urls import url
from app03 import views

app_name = 'app03'
urlpatterns = [
    url(r'^upload/', views.index,name='upload'),
]