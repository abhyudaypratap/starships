# Retrive starships
```
GET /starships
```

__Response__

```json
{
    "id": "1",
    "name": "Belbullab-22 starfighter",
    "hyperdrive_rating": "6"
}
```
# Retrive starships from external api
```
GET /external/starships
```

__Response__

```json
{
    "results": [
        {
            "objectId": "utk70kfdBh",
            "consumables": "6 months",
            "name": "Rebel transport",
            "cargoCapacity": 19000000,
            "passengers": 90,
            "maxAtmospheringSpeed": 650,
            "crew": 6,
            "length": 90,
            "model": "GR-75 medium transport",
            "manufacturer": "Gallofree Yards, Inc.",
            "MGLT": 20,
            "starshipClass": "Medium transport",
            "hyperdriveRating": 4,
            "createdAt": "2019-12-13T19:42:35.165Z",
            "updatedAt": "2019-12-13T19:42:37.828Z",
            "pilots": {
                "__type": "Relation",
                "className": "SWAPI_Character"
            },
            "films": {
                "__type": "Relation",
                "className": "SWAPI_Film"
            }
        }
    ],
    "count": 1
}
```