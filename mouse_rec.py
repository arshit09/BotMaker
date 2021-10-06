from pynput.keyboard import Key, Listener
import pyautogui
import easygui
import time
import os
import sys

sleep_time = 0
flag = 0
custom_sleep_time = ''

open('My Bots\mouse_rec.txt', 'w').close()

easygui.msgbox("Press 'C' to record a click.\nPress 'D' to record a double-click.\nPress 'R' to record a right-click.\n\nPress 'Esc' key to exit.", "Mouse Recorder")

title = "Mouse Recorder"
msg = "Select your choice:\n\n\n1. Add constant sleep time after every click.\n   (you will be asked one time after first click only)\n\n2. Add custom sleep time after every click.\n   (you will be asked everytime for that time after you click.)\n\n3. Keep sleep time most of the time same and let me choose for sometime.\n   (input will be filled up by default, you can change whenever you want)"
choices = ["     1     ", "     2     ", "     3     "]
reply = easygui.buttonbox(msg, title, choices=choices)

def sleeptime():
    time.sleep(0.25)
    msg = "Add your sleep time i.e. time to wait before cliking next."
    sleep_time = easygui.enterbox(msg, title)
    return sleep_time

def custom_sleeptime():
    global custom_sleep_time
    time.sleep(0.25)
    msg = "Add your sleep time i.e. time to wait before cliking next."
    custom_sleep_time = easygui.enterbox(msg, title, custom_sleep_time)
    return custom_sleep_time

def on_press(key):
    global sleep_time
    global flag
    if hasattr(key,'char'):
        if key.char == "c":
            x, y = pyautogui.position()
            with open('My Bots\mouse_rec.txt', 'a') as fout:
                fout.writelines("click " + str(x) + " " + str(y) + '\n')
            pyautogui.click()
            if(int(reply.strip(' ')) == 1):
                if(flag == 0):
                    msg = "Add constant sleep time."
                    sleep_time = easygui.enterbox(msg, title)
                    flag = 1
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleep_time + " 0" + '\n')
            elif(int(reply.strip(' ')) == 2):
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
            elif(int(reply.strip(' ')) == 3):
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + custom_sleeptime() + " 0" + '\n')
        elif key.char == "d":
            x, y = pyautogui.position()
            with open('My Bots\mouse_rec.txt', 'a') as fout:
                fout.writelines("double_click " + str(x) + " " + str(y) + '\n')
            pyautogui.doubleClick()
            if(int(reply.strip(' ')) == 1):
                if(flag == 0):
                    msg = "Add constant sleep time."
                    sleep_time = easygui.enterbox(msg, title)
                    flag = 1
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleep_time + " 0" + '\n')
            elif(int(reply.strip(' ')) == 2):
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
            elif(int(reply.strip(' ')) == 3):
                with open('My Bots\mouse_rec.txt', 'a') as fout:
                    fout.writelines("sleep_time " + custom_sleeptime() + " 0" + '\n')
        elif key.char == "r":
            x, y = pyautogui.position()
            with open('My Bots\mouse_rec.txt', 'a') as fout:
                fout.writelines("right_click " + str(x) + " " + str(y) + '\n')
            pyautogui.rightClick()
    if key == Key.esc:
        msg = 'Mouse movements recorded successfully.\n\nChange default saved file(My Bots\mouse_rec.txt) name?'
        choices = ["Yes", "No"]
        rename = easygui.buttonbox(msg, title, choices=choices)
        if(rename == 'Yes'):
            msg = "Enter your new file name: My Bots\mouse_rec.txt > "
            new_name = easygui.enterbox(msg, title)
            rename_command = 'ren ' + '"My Bots"\mouse_rec.txt ' + new_name + '.txt'
            os.system(rename_command)
            exit()
        elif(rename == 'No'):
            exit()

with Listener(on_press=on_press) as listener:
    listener.join()