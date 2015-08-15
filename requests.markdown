# requests examples, more for my spec purposes, i dont need to expose everything


## customers
trip
* new customer trip

```
POST
xxx/trip/user/<user_id> [gets all trips according to user id]
```

```
{
	'locations': [
		{
			'id': 7623,
			'start':{
				'longitude': 127635,
				'latitude': 2126127
			},
			'end':{
				'longitude': 127635,
				'latitude': 2126127
			}
		},
	]},
	'riders': [
		{<user_object>},
		{<user_object>},
		{<user_object>}
		]
	},
	{
		'scenic': True
	},
	{
		'start_ts':<datetime-object repr>
	}
}
```
'locations' key will specify all start and end points of every line on the graph, you will have to do actual routing to every location

```
PATCH [TO ACCEPT TRIP/ARRIVE AT PICKUP/ARRIVE AT DESINATION]
xxx/trip/123
{
	'status': 'confirmed',
}
```

* profiles

```
GET
xxx/user/rider

{
	'id': 12322,
	'photo': 'www.giphy.com/woah'
	'name': 'Alec',
	'type_of_user': 'rider',
	'phone_number': '416-992-2635'
	'description': ';sjdjbasdjfajsbdf',
	'interests': 'biking, cooking, eating',
	'trips': [<trip-object>]
}


{
	'id': 83463,
	'name': 'Dave',
	'type_of_user': 'customer',
	'phone-number': '416-992-2635'
	'description': ';sjdjbasdjfajsbdf',
	'interests': 'skiing, bbq'ing, eating',
}
```

