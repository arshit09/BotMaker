from pynput.keyboard import Key, Listener
import pyautogui
import time

open('mouse_rec.txt', 'w').close()

def on_press(key):
    if hasattr(key,'char'):
        if key.char == "c":
            x, y = pyautogui.position()
            with open('mouse_rec.txt', 'a') as fout:
                fout.writelines("click " + str(x) + " " + str(y) + '\n')
            pyautogui.click()

        elif key.char == "d":
            x, y = pyautogui.position()
            with open('mouse_rec.txt', 'a') as fout:
                fout.writelines("double_click " + str(x) + " " + str(y) + '\n')
            pyautogui.doubleClick()

    if key == Key.esc:
        exit()

with Listener(on_press=on_press) as listener:
    listener.join()