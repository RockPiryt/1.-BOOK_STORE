import json
import requests

# Define the callAPI function that takes the base and exponent numbers as parameters
def callAPI(base, exponent):
    # Instantiate a headers dictionary
    headers = {
        "Content-Type": "application/json"
    }
    # Create a dictionary with parameters for API call
    payload = {
        "base": base,
        "exponent": exponent
    }
    # Convert the payload dictionary to JSON format
    raw = json.dumps(payload)
    # Define the API endpoint URL
    url = "YOUR API GATEWAY ENDPOINT"
    # Make API call with parameters
    response = requests.post(url, headers=headers, data=raw)
    # Handle response
    if response.status_code == 200:
        # Parse the response body
        result = json.loads(response.text)
        # Display the result
        print(result['body'])
    else:
        print("Error:", response.status_code)

# Example usage:
base = 2
exponent = 3
callAPI(base, exponent)