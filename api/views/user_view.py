from rest_framework.generics import (RetrieveUpdateDestroyAPIView,
                                     ListAPIView)

from users.models import User
from api.serializers import (
    UserSerializer
)
from api.utils.utils import (
    send_unconfirmed
)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return ListAPIView.list(self, request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        if self.request.data.get('trips'):
            phone_number = self.get_object().phone_number
            send_unconfirmed(phone_number)
        return RetrieveUpdateDestroyAPIView.partial_update(
            self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return RetrieveUpdateDestroyAPIView.retrieve(self, request, *args, **kwargs)
