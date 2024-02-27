import requests

#Get response from API
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#Check staus code
code = response.status_code

#Get info about errors (404 - Not Found)
response.raise_for_status()

#Get data in JSON format
data = response.json()
# print(data)


# Get particular info from API
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position =(longitude, latitude)
print(iss_position)