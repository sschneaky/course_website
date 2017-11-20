"""course_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views


urlpatterns = [

    url(r'^$', RedirectView.as_view(url='/calendar')),
    url(r'^calendar', views.CalendarListView.as_view(), name='calendar'),
    url(r'^course', views.Course, name='course'),
    url(r'^projects', views.Projects, name='projects'),
    url(r'^piazza', views.Piazza, name='piazza'),
    url(r'^blackboardGrades', views.BlackboardGrades, name='blackboard_grades'),
    url(r'^blackboard', views.Blackboard, name='blackboard'),
    url(r'^submit', views.Submit, name='submit'),
]
