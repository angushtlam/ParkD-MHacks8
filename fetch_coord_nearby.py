import json
import foursquare

json_data = {}

with open("carpark_data.json") as f:
    json_data = json.loads(f.read())["results"]

if json_data is None:
    print("No data found. Exiting program.")
    exit()

# Connect to foursquare
CLIENT_ID = "OKNO4SRISSXIVQOYDBKBOH4XILQ3ONAMDA2WBBH3WHSD12VL"
CLIENT_SECRET = "0OO2PECNIRQ4EAOIFQZGXJZFJF0XIFKHGWCKNMW0AX1UDEUO"
client = foursquare.Foursquare(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               redirect_uri='http://fondu.com/oauth/authorize')

FS_CATID = {
    "college": "4d4b7105d754a06372d81259",
    "food": "4d4b7105d754a06374d81259",
    "nightlife": "4d4b7105d754a06376d81259",
    "work": "4d4b7105d754a06375d81259"
}

json_output = {}
for carpark in json_data:
    lat = carpark["latitude"]
    long = carpark["longitude"]

    carpark_data = {
        # "id": carpark["id"],
        "location": {
            "latitude": lat,
            "longitude": long
        }
    }

    cat_id_index = 0
    cat_id_keys = list(FS_CATID.keys())
    cat_id_values = list(FS_CATID.values())

    cats_data = {}
    while cat_id_index < len(FS_CATID):
        this_cat_data = []
        cat_name = cat_id_keys[cat_id_index]

        foursquare_resp = client.venues.search(params={
            "ll": str(lat) + "," + str(long),
            "radius": 1000,
            "categoryId": cat_id_values[cat_id_index]
        })

        for venue in foursquare_resp["venues"]:
            this_cat_data.append({
                "name": venue["name"],
                "latitude": venue["location"]["lat"],
                "longitude": venue ["location"]["lng"],
                "check_ins": venue["stats"]["checkinsCount"]
            })

        cats_data.update({cat_name: this_cat_data})

        cat_id_index += 1

    carpark_data.update({"categories": cats_data})
    json_output.update({carpark["id"]: carpark_data})

with open('foursquare_data.json', 'w') as f:
    json.dump({"results": json_output}, f)
