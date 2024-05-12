import requests
import json
from datetime import date

API_URL = "https://api.cricapi.com/v1/cricScore?apikey=dd7c1221-87be-4f95-af10-189499063a70"
API_KEY = "dd7c1221-87be-4f95-af10-189499063a70"

response = requests.get(API_URL)


if response.status_code == 200:
    y = response.json()
    pretty = json.dumps(y['data'], indent = 4)
    for match in y['data']:
        matchdate = match['dateTimeGMT'][0:10]
        todaydate = str(date.today())
        if match['series'] == "Indian Premier League 2024" and matchdate == todaydate :
            print(json.dumps(match, indent = 4))
else:
    print("Serious Error!")