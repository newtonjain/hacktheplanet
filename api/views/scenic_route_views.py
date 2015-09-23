from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bmw.yelp import Yelp


class ScenicRouteCreateView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data.__dict__)
        end_data = request.data.get('end')
        longitude = end_data.get('longitude')
        latitude = end_data.get('latitude')
        yelp_client = Yelp(
            longitude=longitude,
            latitude=latitude)
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
