from rest_framework.generics import (
    ListCreateAPIView
)

from bmw.models import Trip
from address.models import Address
from bmw.serializers import trips


class ScneicRouteCreateView(ListCreateAPIView):
    serializer_class = trips.ScenicRouteSerializer

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)