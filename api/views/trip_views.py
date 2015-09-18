from rest_framework.generics import (RetrieveUpdateDestroyAPIView,
                                     ListCreateAPIView)

from bmw.models import Trip, Driver, Customer
from api.serializers import trips


class TripListCreateView(ListCreateAPIView):
    serializer_class = trips.TripSerializer

    def get_queryset(self):
        driver_pk = self.kwargs.get('driver_pk')
        if driver_pk:
            driver = Driver.objects.get(id=driver_pk)
            return Trip.objects.filter(driver=driver)
        customer_pk = self.kwargs.get('customer_pk')
        if customer_pk:
            customer = Customer.objects.get(id=customer_pk)
            return Trip.objects.filter(customer=customer)
        return Trip.objects.all()

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)


class TripDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = trips.TripSerializer

    def partial_update(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.partial_update(
            self, request, *args, **kwargs)
