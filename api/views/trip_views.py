from rest_framework.generics import (RetrieveUpdateDestroyAPIView,
                                     ListCreateAPIView)
from django.http import Http404

from bmw.models import Trip, Driver, Customer
from api.serializers import trips


class TripListCreateView(ListCreateAPIView):
    serializer_class = trips.TripSerializer
    queryset = Trip.objects.all()

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)


class DriverTripListCreateView(ListCreateAPIView):
    serializer_class = trips.TripSerializer

    def get_queryset(self):
        driver_facebook_id = self.kwargs.get('pk')
        if driver_facebook_id:
            driver = Driver.objects.filter(facebook_id=driver_facebook_id).first()
        if not driver:
            raise Http404
        return Trip.objects.filter(driver=driver)

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)


class CustomerTripListCreateView(ListCreateAPIView):
    serializer_class = trips.TripSerializer

    def get_queryset(self):
        customer_facebook_pk = self.kwargs.get('pk')
        if customer_facebook_pk:
            customer = Customer.objects.filter(facebook_id=customer_facebook_pk).first()
        if not customer:
            raise Http404
        return Trip.objects.filter(customer=customer)

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)


class TripDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = trips.TripSerializer

    def partial_update(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.partial_update(
            self, request, *args, **kwargs)
