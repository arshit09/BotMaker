from pynput.keyboard import Key, Listener
import pyautogui
import time

open('tracker.txt', 'w').close()

def on_press(key):
    if hasattr(key,'char'):
        if key.char == "c":
            x, y = pyautogui.position()
            with open('tracker.txt', 'a') as fout:
                fout.writelines("click " + str(x) + " " + str(y) + '\n')

        if key.char == "d":
            x, y = pyautogui.position()
            with open('tracker.txt', 'a') as fout:
                fout.writelines("double_click " + str(x) + " " + str(y) + '\n')

with Listener(on_press=on_press) as listener:
    listener.join()