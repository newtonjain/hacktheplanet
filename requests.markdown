GET /trip
```
[
    {
        "id": 5,
        "name": "Brian",
        "scenic": false,
        "trip_status": "FINISHED",
        "driver_id": 78,
        "customer_id": 93,
        "start": {
            "id": 5,
            "latitude": "37.7886243731444",
            "longitude": "-122.344195457904"
        },
        "end": {
            "id": 6,
            "latitude": "37.7876579151668",
            "longitude": "-122.343611604231"
        },
        "price": 0
    },
    {
        "id": 6,
        "name": "Brian",
        "scenic": false,
        "trip_status": "PICKING UP",
        "driver_id": 80,
        "customer_id": 89,
        "start": {
            "id": 7,
            "latitude": "37.7877513089559",
            "longitude": "-122.343836672853"
        },
        "end": {
            "id": 8,
            "latitude": "37.7888234519474",
            "longitude": "-122.344186395867"
        },
        "price": 0
    }
]
```

GET /trip/driver/[driver-id]

`gets all trips associated with this driver`

GET /trip/customer/[customer-id]

`gets all trips associated with this customer`

POST /trip

`same as one trip except no trip_status and no price`

GET /driver

```
[
{
    "id": 78,
    "username": "driver0",
    "name": "Gavyn",
    "email": "kemmer.tenika@krajcik.com",
    "description": "",
    "bike_model": "BMW G 650 GS"
}
]
```

GET /customer
```
[
{
    "id": 88,
    "name": "Henderson",
    "email": "yjohnson@hodkiewicz.com",
    "description": ""
}
]
```

GET /transactions

```
{
    'id': 123,
    'driver_id': 2,
    'customer_id': 3,
    'price': 12323
}
```
