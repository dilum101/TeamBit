from django.db import models


class playerMetrics(models.Model):
    
    player_name = models.CharField(max_length=100,null=True,blank=True)
    player_no =  models.CharField(max_length=20,null=True,blank=True)
    player_deviceId = models.CharField(max_length=40,null=True,blank=True)
    group_name = models.CharField(max_length=40)
    session_name = models.CharField(max_length=40,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True) 

    distance = models.FloatField(null=True,blank=True)
    high_speed_distance = models.FloatField(null=True,blank=True)
    sprint_distance = models.FloatField(null=True,blank=True)
    velocity = models.FloatField(null=True,blank=True)
    Workload = models.FloatField(null=True,blank=True)
    long  = models.FloatField(null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    
# Create your models here.
