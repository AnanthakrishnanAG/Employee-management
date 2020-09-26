from django.db import models




class ActivityPeriod(models.Model):
      
     
    # _id=models.CharField(max_length=20,null=False)
 
    start_time=models.DateTimeField(null=False)
    end_time=models.DateTimeField(null=False)
    class Meta:
      db_table = "ActivityPeriod"
    
    # def __str__(self):
    #   return self.name





class User(models.Model):
    _id=models.CharField(max_length=20,null=False)
    real_name=models.CharField(max_length=50,null=False)
    tz=models.CharField(max_length=50,null=False)
    activity_periods=models.ManyToManyField(ActivityPeriod,related_name='activity_periods')
    # period=models.ForeignKey(ActivityPeriod,blank=True,null=True,on_delete=models.CASCADE)
    class Meta:
      db_table = "User"
    # def __str__(self):
    #   return self.name





