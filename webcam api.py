# mYWlNjvyV4YRT8q3vwue9hFAPQpCkCoc
import requests
import time

print("")

api = "https://api.windy.com/api/webcams/v2/list/property=hd"

headers = {
    'x-windy-key':'mYWlNjvyV4YRT8q3vwue9hFAPQpCkCoc'
}
response = requests.get(url=api, headers=headers)

print(response.json())

time.sleep(1)

print("If you cant find any cameras using this method click this link to see all the open webcams listed in the world: https://www.windy.com/?35.102,7.207,3")

time.sleep(20)