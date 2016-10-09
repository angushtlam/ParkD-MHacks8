import json
import csv
import requests

json_output = []

with open("carpark_data.csv") as f:
    reader = csv.DictReader(f)
    
    for row in reader:

        # Declare variables
        addr = row["FacilityAd"]

        google_api_link = "https://maps.googleapis.com/maps/api/geocode/json?address=" + addr.replace(' ', '+') + ",+Detroit,+MI" + "&key=AIzaSyBfzTYqpErU96463MzQqGLHD1mnrW1nnY8"
        req_json = requests.get(google_api_link).json()

        json_output.append({
            "id": row["OBJECTID"],
            "address": addr,
            "latitude": req_json["results"][0]["geometry"]["location"]["lat"],
            "longitude": req_json["results"][0]["geometry"]["location"]["lng"],
            "name": row["FacilityNa"],
            "private": True if (row["PublicPriv"] == "Private") else False,
            "spaces": int(row["TotalSpace"])
        })


with open('carpark_data.json', 'w') as f:
    json.dump({"results": json_output}, f)
