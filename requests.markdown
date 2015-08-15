# requests examples, more for my spec purposes, i dont need to expose everything


## customers
trip
* new customer trip

```
POST
xxx/trip/
```

```
{
	'customer_id': 12343,
	'location': [
		{
			'id': 7623,
			'start':{STILL WORKING ON THIS FIELD},
			'end':{STILL WORKING ON THIS FIELD}
		},
		{
			[WHEN SCENIC IS TRUE, IN THE REQUEST RESPONSE, MORE LOCATIONS WILL BE GIVEN BACK]
		},
	]},
	'riders': [
		{'id': 1232},
		{'id': 2113},
		{'id': 3211}
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

* rider trips

```
GET
xxx/trip/
{
	'trips':[
		[legit the same as POST except when `accepted`]
	]
}
```

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
	'name': 'Alec',
	'type_of_user': 'rider',
	'phone-number': '416-992-2635'
	'description': ';sjdjbasdjfajsbdf',
	'interests': 'biking, cooking, eating',
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

