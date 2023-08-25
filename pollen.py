# pollen forecast program

import requests

# Make a request to the Breezometer API to retrieve the daily pollen forecast for the next 3 days
response = requests.get('https://api.breezometer.com/pollen/v2/forecast/daily?lat=44.8341639&lon=-87.3770419&days=3&key=54dcffdf034a404bbb76d57e739a7703')

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Loop through the pollen data for each day and display the forecast to the user
    for day_data in data['data']:
        date = day_data['date']
        grass_value = day_data['types']['grass']['index']['category']
        tree_value = day_data['types']['tree']['index']['category']
        weed_value = day_data['types']['weed']['index']['category']
        print(f"{date} - Grass: {grass_value}, Tree: {tree_value}, Weed: {weed_value}")
else:
    # Handle the error
    print(f"Error: {response.status_code} - {response.text}")