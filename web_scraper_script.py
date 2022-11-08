#web_scraper_script
import requests
from bs4 import BeautifulSoup
import time

exit = ["exit"]

print('''
 ██▓ ███▄    █   █████▒▒█████  ▄▄▄█████▓ ▄▄▄       ██ ▄█▀▓█████  ██▀███  
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒▓  ██▒ ▓▒▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒▒ ▓██░ ▒░▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░░ ▓██▓ ░ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░  ▒██▒ ░  ▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░   ▒ ░░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░     ░      ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒    ░        ░   ▒   ░ ░░ ░    ░     ░░   ░ 
 ░           ░            ░ ░                 ░  ░░  ░      ░  ░   ░     
                                By: 123xboxlookup
                                ''')

scraper = input("enter URL you want to scrape: ")

time.sleep(2)

req = requests.get(f"{scraper}")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

response = ''
while response not in exit:

    response = input("Type 'exit' when you what to exit: ")

if response == 'exit':
    quit()

