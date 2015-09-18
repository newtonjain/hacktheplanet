from rest_framework import serializers

from bmw.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'driver_id', 'price']
