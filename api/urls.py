from django.conf.urls import patterns, url

from .views import (
    trip_views
)

urlpatterns = patterns(
    'views',

    # trips
    url(r'^trip/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/driver/(?P<driver_pk>\d+)/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/customer/(?P<customer_pk>\d+)/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/(?P<pk>\d+)/?$',
        trip_views.TripDetail.as_view(),
        name='trip_api'
        ),

)
