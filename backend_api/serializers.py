from rest_framework import serializers
from .models import playerMetrics

class playerMetrics_serializer(serializers.ModelSerializer):
    class Meta:
        model = playerMetrics
        fields = ('id', 'player_name', 'player_no','group_name','player_deviceId','session_name','date','distance','high_speed_distance','sprint_distance','velocity','Workload','long','lat')