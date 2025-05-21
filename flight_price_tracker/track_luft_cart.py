print("Starting Lufthansa scraper...")

import requests

# Define variables for origin, destination, dates, cabin class, and price threshold
origin = "FRA"  # Frankfurt
destination = "SOF"  # Sofia, Bulgaria
departure_date = "2025-09-04"  # Example departure date
return_date = "2025-09-06"  # Example return date
price_threshold = 150  # Budget threshold for price

# Define the API URL with placeholders, including the service parameter for best price
url = f"https://api.lufthansa.com/v1/promotions/priceoffers/flights/ond/{origin}/{destination}?departureDate={departure_date}&returnDate={return_date}&service=amadeusBestPrice"

# Add authorization header
headers = {
    "Authorization": "Bearer xf9brgn4t6zrjh35y35wcg6n",  # Replace with your actual token
    # qtnbs62gyujnmrkghavyfdwj #5wjupjfut2fngcgj6s62avcg
    "Accept": "application/json",
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant information from the response
    try:
        best_price = data['price']['amount']
        currency = data['price']['currency']
        offer_type = data['offerType']

        print(f"Best price for your flight from {origin} to {destination}: {best_price} {currency} ({offer_type})")

        # Check if the price is within the budget
        if best_price <= price_threshold:
            print("This price is within your budget!")
        else:
            print("This price is above your budget.")

    except KeyError:
        print("Error: Could not retrieve price information.")
else:
    print(f"Error: {response.status_code} - {response.text}")



print("Finished scraping.")