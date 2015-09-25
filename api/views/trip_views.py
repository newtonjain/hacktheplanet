from rest_framework.generics import (RetrieveUpdateDestroyAPIView,
                                     ListCreateAPIView)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from bmw.models import Trip, Driver, Customer, TripStatus
from api.serializers import trips
from api.utils.utils import (
    send_confirmed,
    send_arrived
)


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
        return Trip.objects.filter(
            driver=driver).exclude(
            trip_status__name='FINISHED')

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


class TripStatusDetailView(APIView):

    def post(self, request, *args, **kwargs):
        trip_id = request.data.get('id')
        trip = Trip.objects.filter(id=trip_id).first()
        new_status = request.data.get('trip_status')
        if trip:
            if new_status == 'PICKING UP' and trip.trip_status.name == 'REQUESTED':
                print('sending confirmed text')
                send_confirmed(trip.customer.phone_number)
                trip.trip_status = TripStatus.objects.get(name='PICKING UP')
            if new_status == 'ARRIVED' and trip.trip_status.name == 'PICKING UP':
                trip.trip_status = TripStatus.objects.get(name='ARRIVED')
                print('send arrived text')
                send_arrived(trip.customer.phone_number)
            if new_status == 'FINISHED' and trip.trip_status.name == 'ARRIVED':
                trip.trip_status = TripStatus.objects.get(name='FINISHED')
        result = {}
        result['id'] = trip_id
        result['trip_status'] = trip.trip_status.name
        trip.save()
        return Response(result, status=status.HTTP_200_OK)
