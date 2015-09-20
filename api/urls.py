from django.conf.urls import patterns, url

from .views import (
    trip_views,
    driver_views,
    customer_views,
    transaction_views
)

urlpatterns = patterns(
    'views',

    # trips
    url(r'^trip/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/driver/(?P<pk>\d+)/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/customer/(?P<pk>\d+)/?$',
        trip_views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    # JUST CURRENTLY SUPPORTS PATCHING TRIP_STATUS
    url(r'^trip/(?P<pk>\d+)/?$',
        trip_views.TripDetail.as_view(),
        name='trip_api'
        ),

    # driver
    url(r'^driver/?$',
        driver_views.DriverListCreateView.as_view(),
        name='driver_api'
        ),
    url(r'^driver/(?P<pk>\d+)/?$',
        driver_views.DriverDetailView.as_view(),
        name='driver_api'
        ),

    # customer
    url(r'^customer/?$',
        customer_views.CustomerListCreateView.as_view(),
        name='customer_api'
        ),
    url(r'^customer/(?P<pk>\d+)/?$',
        customer_views.CustomerDetailView.as_view(),
        name='customer_api'
        ),

    # transactions
    url(r'^transaction/?$',
        transaction_views.TransactionListCreateView.as_view(),
        name='transaction_api'
        ),
)
