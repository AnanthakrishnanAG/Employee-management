from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse

from .models import ActivityPeriod,User
from . serializers import UserSerializer,ActivityPeriodsSerializer
from rest_framework import viewsets









class EmpView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 
class ActivityPeriodView(viewsets.ModelViewSet):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodsSerializer
    


