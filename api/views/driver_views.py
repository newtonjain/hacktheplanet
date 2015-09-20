from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from django.http import Http404

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

    def get_object(self):
        facebook_id = int(self.kwargs.get('pk'))
        obj = Driver.objects.filter(facebook_id=facebook_id).first()
        if not obj:
            raise Http404
        return obj

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
