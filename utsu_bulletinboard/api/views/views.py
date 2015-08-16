
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)

from api.models import Trip, Location
from users.models import User
from api.serializers import (
    UserSerializer,
    TripSerializer,
)


class TripListCreateView(ListAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    # def get_queryset(self):
    #     user_id = self.kwargs.get('pk')
    #     user = User.object.get(id=user_id)
    #     return user.trips

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return ListCreateAPIView.create(self, request, *args, **kwargs)

# class TripCreateView(ListCreateAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer

#     def create(self, request, *args, **kwargs):
#         return ListCreateAPIView.create(self, request, *args, **kwargs)


class TripDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def partial_update(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.partial_update(
            self, request, *args, **kwargs)


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return ListCreateAPIView.list(self, request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
