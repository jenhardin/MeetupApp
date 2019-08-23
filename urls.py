from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.meetup, name='meetup'),
    path('<str:name>', views.GroupName, name='GroupName'),
]

urlpatterns += staticfiles_urlpatterns()

