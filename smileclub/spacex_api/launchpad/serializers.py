from rest_framework import serializers
from .models import LaunchPad

class LaunchPadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaunchPad
        fields = ('lp_id', 'lp_name', 'lp_status')

