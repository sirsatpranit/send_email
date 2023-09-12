from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from employee.models import employee, event, log
from employee.serializers import EmployeeSerializer, EventSerializer, LogSerializer 

# Create your views here.
def home(request):
    return HttpResponse("Initial setup")
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = event.objects.all()
    serializer_class = EventSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = log.objects.all()
    serializer_class = LogSerializer