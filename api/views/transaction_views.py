from rest_framework.generics import (
    ListCreateAPIView
)

from bmw.models import Transaction
from api.serializers import transactions


class TransactionListCreateView(ListCreateAPIView):
    serializer_class = transactions.TransactionSerializer
    queryset = Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)
