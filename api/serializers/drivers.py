from rest_framework import serializers

from bmw.models import Driver


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ['id', 'username', 'name', 'email', 'description',
                  'bike_model']
