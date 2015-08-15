from django.conf.urls import patterns, url

urlpatterns = patterns(
    'views',

   	# trips
    url(r'^trip/?$',
        event_views.TripCreateView.as_view(),
        name='trip_api'
        ),
    url(r'^trip/user/(?P<user_pk>\d+)/?$',
        event_views.TripList.as_view(),
        name='trip_api'
        ),
    url(r'^trip/(?P<pk>\d+)/?$',
        event_views.TripDetail.as_view(),
        name='trip_api'
        ),

    # users
    url(r'^user/?$',
        event_views.UserListView.as_view(),
        name='user_api'
        ),


)
