from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import ListView
from django.utils import timezone

from .models import ClassPeriod
# Create your views here.

class CalendarListView(ListView):

	model = ClassPeriod

	def get_context_data(self, **kwargs):
		context = super(CalendarListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['next_class'] = ClassPeriod.objects.filter(date__gte=timezone.now()).first()
		return context

	template_name = 'calendar.html'

def Projects(request):
	return render(request, "projects.html")

def Course(request):
	return render(request, "course.html")

def Piazza(request):
	return render(request, "piazza.html")

def Blackboard(request):
	return render(request, "blackboard.html")

def BlackboardGrades(request):
	return render(request, "blackboardGrades.html")

def Submit(request):
	return render(request, "submit.html")

