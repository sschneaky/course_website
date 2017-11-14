from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

def calendar(request):
	return render(request, "calendar.html")


def projects(request):
	return render(request, "projects.html")


def course(request):
	return render(request, "course.html")

def piazza(request):
	return render(request, "piazza.html")

def blackboard(request):
	return render(request, "blackboard.html")