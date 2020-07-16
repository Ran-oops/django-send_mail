from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^mail/', views.mail, name='mail'),
]