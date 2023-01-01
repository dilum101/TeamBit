from dataclasses import fields
from rest_framework import serializers
from .models import Unreg_Users,Reg_Users
from .models import Training_Session

class UnReg_serializer(serializers.ModelSerializer):
    class Meta:
        model = Unreg_Users
        fields = ("email")
     
        
class Reg_Users_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Users
        fields = ("id","user_name","password","email_id")             
    
    def create(self, validated_data):
        return super().create(validated_data)    
    
    def getPassword(self):
        return self.password

class Training_Session_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training_Session
        fields = ("__all__")             
    

    def getDate(self):
        return self.training_date
    
    def getTraining_session_name(self):
        return self.training_session_name
    
    def getDistance_travelled(self):
        return self.distance_travelled
    
    def getHigh_speed_distance(self):
        return self.high_speed_distance_travelled
    
    def getSprint_distance(self):
        return self.sprint_distance_travelled

    def getPlayer_veloity(self):
        return self.player_veloity        
    
    def getPlayer_position(self):
        return self.player_position
