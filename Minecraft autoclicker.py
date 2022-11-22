import os
import sys
import threading
import time

from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller

divider = "————————————————————————————————————————————————————————"

print("""                                                   
 ██▓ ███▄    █   █████▒▒█████   ▄████▄   ██▓     ██▓ ▄████▄   ██ ▄█▀▓█████  ██▀███     
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒   
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒   
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄     
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒   
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░   
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░   ░  ▒   ░ ░ ▒  ░ ▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░   
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  ░          ░ ░    ▒ ░░        ░ ░░ ░    ░     ░░   ░    
 ░           ░            ░ ░  ░ ░          ░  ░ ░  ░ ░      ░  ░      ░  ░   ░        
                               ░                    ░                                                                                                   
""")

print(divider)

try:
    clicks = float(input("- Enter delay speed (Reccomended 0.1 or 9CPS for minecraft): "))
    delay = clicks
except ValueError:
    clicks = 0.060
    delay = clicks

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_start_and_stop_key = str(input("- Choose start and stop key (Default: x): "))
start_stop_key = KeyCode(char=input_start_and_stop_key)

if input_start_and_stop_key == "":
    start_stop_key = KeyCode(char="x")

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_exit_key = str(input("- Exit key (Default: `): "))
exit_key = KeyCode(char=input_exit_key)

if input_exit_key == "":
    exit_key = KeyCode(char="`")

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_button = str(input("- Options: Left, Right, Middle"
                         "\nMouse button: (Default: Left Mouse Button): "))

input_button = input_button.lower()
button = Button.left

if input_button == "right":
    button = Button.right
elif input_button == "middle":
    button = Button.middle
else:
    pass

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


def check_os():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


print("- The InfoClicker is Online")
check_os()

print("- The InfoClicker is Offline")
print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()

            check_os()

            print("- The InfoClicker is Offline")
            print(divider)
        else:
            click_thread.start_clicking()

            check_os()

            print("- The InfoClicker is Online")
            print(divider)
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()