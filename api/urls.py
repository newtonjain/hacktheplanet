from django.conf.urls import patterns, url

from .views import views

urlpatterns = patterns(
    'views',

    # trips
    url(r'^trip/?$',
        views.TripListCreateView.as_view(),
        name='trip_api'
        ),
    # url(r'^trip/user/(?P<pk>\d+)/?$',
    #     views.TripListView.as_view(),
    #     name='trip_api'
    #     ),
    url(r'^trip/(?P<pk>\d+)/?$',
        views.TripDetail.as_view(),
        name='trip_api'
        ),
    # users
    url(r'^user/?$',
        views.UserListView.as_view(),
        name='user_api'
        ),
    url(r'^user/(?P<pk>\d+)/?$',
        views.UserDetailView.as_view(),
        name='user_api'
        ),



)
