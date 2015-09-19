from rest_framework import serializers

from bmw.models import Transaction, Driver, Customer


class TransactionSerializer(serializers.ModelSerializer):
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all())
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())

    class Meta:
        model = Transaction
        fields = ['id', 'driver_id', 'customer_id', 'price']
