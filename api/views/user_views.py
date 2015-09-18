from rest_framework.generics import RetrieveUpdateDestroyAPIView
from itertools import chain

from bmw.models import Driver, Customer
from api.serializers.users import UserDetailSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return list(chain(Driver.objects.all(), Customer.objects.all()))

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
