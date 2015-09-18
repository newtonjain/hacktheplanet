from django.conf.urls import patterns, url

from .views import (
    trip_views,
    user_views,
    driver_views,
    customer_views
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

    # users
    url(r'^user/(?P<user_pk>\d+)/?$',
        user_views.UserDetailView.as_view(),
        name='user_api'
        ),

    # driver
    url(r'^driver/?$',
        driver_views.DriverListCreateView.as_view(),
        name='driver_api'
        ),
    url(r'^driver/(?P<driver_pk>\d+)/?$',
        driver_views.DriverDetailView.as_view(),
        name='driver_api'
        ),

    # customer
    url(r'^customer/?$',
        customer_views.CustomerListCreateView.as_view(),
        name='customer_api'
        ),
    url(r'^customer/(?P<customer_pk>\d+)/?$',
        customer_views.CustomerDetailView.as_view(),
        name='customer_api'
        ),
)
