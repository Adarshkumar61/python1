import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"#from a web off currency rates of real time

response = requests.get(API_URL)

rates = response.json()["rates"]

amount = float(input("Enter amount in USD: "))

currency = input("Enter currency code (e.g., INR, EUR): ").upper()

if currency in rates:
    print(f"{amount} USD = {amount * rates[currency]} {currency}")
else:
    print("Currency not supported.")