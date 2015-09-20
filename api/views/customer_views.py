from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from django.http import Http404

from bmw.models import Customer
from api.serializers.customers import (CustomerSerializer)


class CustomerListCreateView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get_object(self):
        facebook_id = int(self.kwargs.get('pk'))
        obj = Customer.objects.filter(facebook_id=facebook_id).first()
        if not obj:
            raise Http404
        return obj

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
