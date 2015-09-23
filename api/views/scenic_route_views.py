from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bmw.yelp import Yelp


class ScenicRouteCreateView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.data.__dict__)
        yelp_client = Yelp(
            longitude=0,
            latitude=0)
        yelp_location_data = yelp_client.get_locations()
        print(yelp_location_data)
        result = []
        for location in yelp_location_data['businesses']:
            coordinate = location['location'].get('coordinate')
            if coordinate:
                result.append({
                    'latitude': coordinate.get('latitude'),
                    'longitude': coordinate.get('longitude')})
        return Response(result, status=status.HTTP_200_OK)
