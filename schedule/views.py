from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse

from .models import ActivityPeriod,User
from . serializers import UserSerializer,ActivityPeriodsSerializer
from rest_framework import viewsets
from rest_framework.response import Response


#view for the emp-list


class EmpView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    

#view for the activity period list
class ActivityPeriodView(viewsets.ModelViewSet):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodsSerializer
    

