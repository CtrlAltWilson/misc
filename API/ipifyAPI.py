"""
API call to get the external IP address of the machine running the script
"""

import requests
response = requests.get('https://api.ipify.org')
print(response.text)
