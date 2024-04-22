"""
API Call to MyCurrencyCollection to check the rarity of US bank note serial numbers.

"""

import requests
import json

url = "https://www.mycurrencycollection.com/reference/fancy-serial-number-checker"

data = {"serial_number": "87298349"}

response = requests.post(url, json=data)

print(response.text)
