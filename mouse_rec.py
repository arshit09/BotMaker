from pynput.keyboard import Key, Listener
from time import gmtime, strftime
import pyautogui
import easygui
import time
import os
import cv2
import numpy as np

sleep_time = 0
flag = 0
custom_sleep_time = ''
currenttime = strftime("%dd%mm%Yy%Hhr%Mm%Ss", gmtime())
botfilepath = '.\\My Bots\\' + currenttime + '.txt'
# for screenshots
xy = []
# ------------------------

if easygui.msgbox("Press 'C' to record a click.\nPress 'D' to record a double-click.\nPress 'R' to record a right-click.\nTo take screenshot: \n   Press '1' to record one corner.\n   Press '2' to record another corner.\n\nPress 'Esc' key to exit.", "Mouse Recorder") is None:
    exit()

title = "Mouse Recorder"
msg = "Select your choice:\n\n\n1. Add constant sleep time after every click.\n   (you will be asked one time after first click only)\n\n2. Add custom sleep time after every click.\n   (you will be asked everytime for that time after you click.)\n\n3. Keep sleep time most of the time same and let me choose for sometime.\n   (input will be filled up by default, you can change whenever you want)"
choices = ["     1     ", "     2     ", "     3     "]
reply = easygui.buttonbox(msg, title, choices=choices)
if reply is None:
    exit()

def takeSS():
    topL = []
    topR = []
    botL = []
    botR = []
    global sleep_time
    global flag
    global xy
    global currenttime
    global botfilepath
    def position(x1, y1, x2, y2):
        if(y1 > y2):
            if(x1 > x2):
                botR.append(x1)
                botR.append(y1)
            else:
                botL.append(x1)
                botL.append(y1)
        else:
            if(x1 > x2):
                topR.append(x1)
                topR.append(y1)
            else:
                topL.append(x1)
                topL.append(y1)

    position(xy[0],xy[1],xy[2],xy[3])
    position(xy[2],xy[3],xy[0],xy[1])

    if ((not topL) and (not botR)):
        topL.append(botL[0])
        topL.append(topR[1])
        botR.append(topR[0])
        botR.append(botL[1])

    # print("-"*30)
    # print("|",topL,"            ", topR,"\n|\n|\n|\n|", botL,"          ", botR)

    image = pyautogui.screenshot(region=(topL[0], topL[1], botR[0]-topL[0], botR[1]-topL[1]))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    now = './My Bots/' + strftime("%dd%mm%Yy%Hhr%Mm%Ss", gmtime()) + '.png'
    cv2.imwrite(now, image)
    with open(botfilepath, 'a') as fout:
        fout.writelines("screenshot " + now[10:] + " 0" + '\n')
    if(int(reply.strip(' ')) == 1):
        if(flag == 0):
            msg = "Add constant sleep time."
            sleep_time = easygui.enterbox(msg, title)
            flag = 1
        with open(botfilepath, 'a') as fout:
            fout.writelines("sleep_time " + sleep_time + " 0" + '\n')
    elif(int(reply.strip(' ')) == 2):
        with open(botfilepath, 'a') as fout:
            fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
    elif(int(reply.strip(' ')) == 3):
        with open(botfilepath, 'a') as fout:
            fout.writelines("sleep_time " + custom_sleeptime() + " 0" + '\n')

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
    global xy
    global currenttime
    botfilepath = '.\\My Bots\\' + currenttime + '.txt'
    if hasattr(key,'char'):
        if key.char == "c":
            x, y = pyautogui.position()
            with open(botfilepath, 'a') as fout:
                fout.writelines("click " + str(x) + " " + str(y) + '\n')
            pyautogui.click()
            if(int(reply.strip(' ')) == 1):
                if(flag == 0):
                    msg = "Add constant sleep time."
                    sleep_time = easygui.enterbox(msg, title)
                    flag = 1
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + sleep_time + " 0" + '\n')
            elif(int(reply.strip(' ')) == 2):
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
            elif(int(reply.strip(' ')) == 3):
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + custom_sleeptime() + " 0" + '\n')
        elif key.char == "d":
            x, y = pyautogui.position()
            with open(botfilepath, 'a') as fout:
                fout.writelines("double_click " + str(x) + " " + str(y) + '\n')
            pyautogui.doubleClick()
            if(int(reply.strip(' ')) == 1):
                if(flag == 0):
                    msg = "Add constant sleep time."
                    sleep_time = easygui.enterbox(msg, title)
                    flag = 1
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + sleep_time + " 0" + '\n')
            elif(int(reply.strip(' ')) == 2):
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + sleeptime() + " 0" + '\n')
            elif(int(reply.strip(' ')) == 3):
                with open(botfilepath, 'a') as fout:
                    fout.writelines("sleep_time " + custom_sleeptime() + " 0" + '\n')
        elif key.char == "r":
            x, y = pyautogui.position()
            with open(botfilepath, 'a') as fout:
                fout.writelines("right_click " + str(x) + " " + str(y) + '\n')
            pyautogui.rightClick()
        elif key.char == "1":
            x1, y1 = pyautogui.position()
            xy.append(x1)
            xy.append(y1)
        elif key.char == "2":
            x2, y2 = pyautogui.position()
            xy.append(x2)
            xy.append(y2)
            takeSS()

    if key == Key.esc:
        msg = 'Mouse movements recorded successfully.\n\nPlease save your bot file'
        new_name = easygui.enterbox(msg, title, botfilepath[10:-4])
        rename_command = 'ren ' + '"My Bots"\\' + botfilepath[10:] + ' ' + new_name + '.txt'
        os.system(rename_command)
        exit()

with Listener(on_press=on_press) as listener:
    listener.join()