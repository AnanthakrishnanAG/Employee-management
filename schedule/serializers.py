from rest_framework import serializers
from . models import User,ActivityPeriod

class ActivityPeriodsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ActivityPeriod
        fields=('start_time','end_time')


class UserSerializer(serializers.ModelSerializer):
    activity_periods=ActivityPeriodsSerializer(many=True,read_only=True)
    class Meta:
        model=User
        fields=('_id','real_name','tz','activity_periods')
        depth=1
        




   

    # def get_exercises(self, obj):
    #         qs = obj.periods.all().order_by('index')
    #         return UserSerializer(qs, many=True, read_only=True).data
