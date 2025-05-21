from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
client = ApifyClient("YOUR_APIFY_API_TOKEN")

# Prepare the Actor input
run_input = {
    "FROM": "FRA",
    "TO": "SOF",
    "DATE_FROM": "01/09/2025",
    "DATE_TO": "30/09/2025",
    "NIGHTS_IN_DST_FROM": 1,
    "NIGHTS_IN_DST_TO": 3,
    "CURRENCY": "EUR"
}

# Run the Actor and wait for it to finish
run = client.actor("scraped/flight-price-trends").call(run_input=run_input)

# Fetch and print the results
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    price = item.get("price")
    departure = item.get("departure")
    return_date = item.get("return")
    link = item.get("link")
    print(f"€{price} | Depart: {departure} | Return: {return_date}")
    print(f"Link: {link}")
