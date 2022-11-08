#youtube_viewbot
import webbrowser, time

print('''                      __       ___.                  .__              ___.           __   
 ___.__. ____  __ ___/  |_ __ _\_ |__   ____   ___  _|__| ______  _  _\_ |__   _____/  |_ 
<   |  |/  _ \|  |  \   __\  |  \ __ \_/ __ \  \  \/ /  |/ __ \ \/ \/ /| __ \ /  _ \   __|
 \___  (  <_> )  |  /|  | |  |  / \_\ \  ___/   \   /|  \  ___/\     / | \_\ (  <_> )  |  
 / ____|\____/|____/ |__| |____/|___  /\___  >   \_/ |__|\___  >\/\_/  |___  /\____/|__|  
 \/                                 \/     \/                \/            \/           
                                                                
                                    By: 123xboxlookup
                                    ''')

time.sleep(1)

url = input("Enter url: ")
views = input("Enter amount of views: ")
duration = input("Enter duration before opening another video (in seconds): ")

for i in range(int(views)):
    webbrowser.open_new(url)
    time.sleep(int(duration))