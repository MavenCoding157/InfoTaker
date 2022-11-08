import requests
import json
import time

response = requests.get(f"http://ip-api.com/json/").content

data = json.loads(response)

print(f"""
IP: {data['query']}
Country: {data['country']}
City: {data['city']}
ZIP: {data['zip']}
ISP: {data['isp']}
Lon: {data['lon']}
Lat: {data['lat']}
""")

time.sleep(5)