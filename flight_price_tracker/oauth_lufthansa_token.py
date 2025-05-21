import requests

# Replace with your actual client ID and client secret
client_id = "csvsmsv23pd4f6ujzwphfsshw"
client_secret = "4ff3rRrDaZ"

# Prepare the payload for the POST request
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# Make the POST request to get the access token
response = requests.post("https://api.lufthansa.com/v1/oauth/token", data=data)

# Check if the request was successful
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get("access_token")
    print("Access Token:", access_token)
else:
    print(f"Error: {response.status_code} - {response.text}")
