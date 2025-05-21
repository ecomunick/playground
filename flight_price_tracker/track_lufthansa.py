from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # add this
import time

print("Starting Lufthansa scraper...")

# Set up Chrome browser (headless mode means no UI will pop up)
options = Options()
options.add_argument("--headless")  # run without GUI
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Updated way to define ChromeDriver path using Service
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)


# Open Lufthansa flight search URL
# url = "https://www.lufthansa.com/de/en/homepage"
# driver.get(url)
#driver.get("https://www.lufthansa.com/de/en/flight-search?origin=FRA&destination=SOF&tripType=2&cabinClass=E&adults=1&departureDate=2025-09-01&returnDate=2025-09-03")
driver.get("https://shop.lufthansa.com/booking/availability/0")
time.sleep(10)  # wait for the page to load
print("Page title:", driver.title) # Confirm page loaded by printing title

# Scrape the price (using the class you provided)
try:
    price_element = driver.find_element(By.CLASS_NAME, "price-amount")
    price = price_element.text
    print("Lowest price found:", price)
except Exception as e:
    print("Error while scraping price:", e)

# Close the browser
driver.quit()

print("Finished scraping.")