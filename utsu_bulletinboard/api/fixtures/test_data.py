from datetime import datetime, timedelta

from api.models import *


class DataBuilder(object):

        @cached_property
        def events(self):
            data = {}

            red = Color.objects.create(
                name='red',
                color='#FF0000'
            )

            blue = Color.objects.create(
                name='blue',
                color='#3333FF'
            )

            yellow = Color.objects.create(
                name='yellow',
                color='#FFFF66'
            )

            green = Color.objects.create(
                name='green',
                color='#66FF33'
            )

            club = Club.objects.create(
                id=9000,
                name='UTSU'
            )
            club.club_colors.add(red, blue, yellow, green)

            page = Page.objects.create()
            page.page_colors.add(red, blue, yellow, green)

            Event.objects.create(
                name='Summer Hot Dog Zinger',
                description='A hot summer has come upon us, why not cool down' +
                            'with a cool hot zinger going down your throat?' +
                            'Lots of beer and hookers will be at this one,' +
                            'so you better make sure not to miss this one.',
                short_description='Beer and hot zingers.',
                start_ts=datetime.now(),
                end_ts=datetime.now() + timedelta(days=2)
                club=club
            )

            return {
                event.name: event for event in Event.objects.all()
            }
