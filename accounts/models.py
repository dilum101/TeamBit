from tkinter import CASCADE
from django.db import models

class Unreg_Users(models.Model):
    email = models.EmailField(max_length=256,primary_key=True)


class Reg_Users(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.ForeignKey(Unreg_Users,on_delete=models.CASCADE)
    password = models.CharField(max_length=100)


class Coach(models.Model):
    coach_id = models.CharField(max_length=100,primary_key=True)
    coach_name = models.CharField(max_length=200)  
    date_of_birth = models.DateField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=500)
    phone_number =models.CharField(max_length=25)
    group_id = models.CharField(max_length=100)

class Player(models.Model):
    player_id = models.CharField(max_length=100,primary_key=True)
    player_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=500)
    phone_number =models.CharField(max_length=25)
    group_id = models.CharField(max_length=100)

class Training_Session(models.Model):
    training_session_name = models.CharField(max_length=500)
    training_date = models.CharField(max_length=50)
    coach_id = models.CharField(max_length=100)
    group_id = models.CharField(max_length=100)
    player_id = models.CharField(max_length=100)
    distance_travelled = models.FloatField(default=0.0)
    high_speed_distance_travelled = models.FloatField(default=0.0)
    sprint_distance_travelled = models.FloatField(default=0.0)
    player_veloity = models.FloatField(default=0.0)
    player_workload = models.IntegerField(0)
    player_position = models.CharField(max_length=500)


class Metric(models.Model):
    metric_id = models.CharField(max_length=100,primary_key=True)
    group_performance = models.CharField(max_length=500)
    player_comparison = models.IntegerField()
    player_id = models.CharField(max_length=100)

class Group(models.Model):
    group_id = models.CharField(max_length=100,primary_key=True)
    group_name = models.CharField(max_length=200)
    coach_id = models.CharField(max_length=100)          
    player_id = models.CharField(max_length=100)
