from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)

from bmw.models import Driver
from api.serializers import drivers


class DriverListCreateView(ListCreateAPIView):
    serializer_class = drivers.DriverSerializer
    queryset = Driver.objects.all()

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)


class DriverDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = drivers.DriverSerializer
    queryset = Driver.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
