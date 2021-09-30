from pynput.keyboard import Key, Listener
import pyautogui
import easygui
import time

open('mouse_rec.txt', 'w').close()

title = "Mouse Recorder"
msg = "Select your choice\n\n\n1. Add constant sleep time after every click.\n\n2. Add custom sleep time after every click.\n   (you will be asked everytime for that time after you click.)\n\n3. Keep sleep time most of the time same and let me choose for sometime.\n   (input will be filled up by default, you can change whenever you want)"
choices = ["     1     ", "     2     ", "     3     "]
reply = easygui.buttonbox(msg, title, choices=choices)

def sleeptime():
    title = "Mouse Recorder"
    msg = "Add your sleep time i.e. time to wait before cliking next."
    sleep_time = easygui.enterbox(msg, title)
    return sleep_time

def on_press(key):
    if hasattr(key,'char'):
        if key.char == "c":
            x, y = pyautogui.position()
            with open('mouse_rec.txt', 'a') as fout:
                fout.writelines("click " + str(x) + " " + str(y) + '\n')
            pyautogui.click()
            if(int(reply.strip(' ')) == 2):
                with open('mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
            

        elif key.char == "d":
            x, y = pyautogui.position()
            with open('mouse_rec.txt', 'a') as fout:
                fout.writelines("double_click " + str(x) + " " + str(y) + '\n')
            pyautogui.doubleClick()
            if(int(reply.strip(' ')) == 2):
                with open('mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')

    if key == Key.esc:
        title = "Mouse Recorder"
        msg = 'Mouse movements recorded successfully.'
        easygui.msgbox(msg, title)
        exit()

with Listener(on_press=on_press) as listener:
    listener.join()