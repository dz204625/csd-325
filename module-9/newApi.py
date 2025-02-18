import requests
import json

# api response
response = requests.get("https://swapi.dev/api/people/") 
# print status code
print(response.status_code)

# print unformatted response
print(response.json())

# get formatted response
formattedResponse = json.dumps(response.json(), sort_keys=True, indent=4)

# print formatted response
print(formattedResponse)