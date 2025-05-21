import requests

# https://developer.lufthansa.com/apps/mykeys

url = "https://api.lufthansa.com/v1/oauth/token"
data = {
    'client_id': 'csvsmsv23pd4f6ujzwphfsshw',  # Replace with your client ID
    'client_secret': '4ff3rRrDaZ',  # Replace with your client secret
    'grant_type': 'client_credentials'
}

response = requests.post(url, data=data)

if response.status_code == 200:
    access_token = response.json().get('access_token')
    print("Access Token:", access_token)
else:
    print("Error:", response.status_code, response.text)
