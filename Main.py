import requests
import json
import googlemaps



response = requests.get("http://www.7timer.info/bin/api.pl?lon=0.12&lat=51.50&product=astro&output=json")
print(response.status_code)

print(type(response.json()))


with open("database.txt","w") as db:
    db.writelines(json.dumps(
    response.json(),
    sort_keys=True,
    indent=4,
    separators=(',', ': ')
))
db.close()

with open("api_key.txt","r") as key_file:
    key = key_file.readline().strip()
    key_file.close()
    



data = response.json()
print(len(data))

for datum in data:
    print(datum)