from rest_framework import serializers
import random

from bmw.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'description', 'facebook_id',
                  'phone_number', 'profile_picture_url']

    def create(self, validated_data):
        customer = Customer.objects.create(
            username=str(random.uniform(0.0, 1.0)),
            **validated_data
        )
        return customer
