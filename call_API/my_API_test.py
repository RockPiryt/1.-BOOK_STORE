import requests

#Get response from API
response = requests.get(url="https://0z8oc0da09.execute-api.eu-west-1.amazonaws.com/Dev/books")

#Check staus code
code = response.status_code

#Get info about errors (404 - Not Found)
response.raise_for_status()

#Get data in JSON format
data = response.json()
# print(data)


# # Get particular info from API
first_book_author = data[0]["author"]
print(first_book_author)
