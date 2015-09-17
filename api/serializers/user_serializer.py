from rest_framework import serializers

from api.models import Trip
from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    trips = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Trip.objects.all())

    class Meta:
        model = User
        fields = ['id', 'photo', 'username',
                  'first_name', 'is_customer', 'phone_number',
                  'description', 'trips', 'interests']
