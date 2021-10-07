from pynput.keyboard import Key, Listener
from time import gmtime, strftime
import pyautogui
import easygui
import time
import os
import cv2
import numpy as np


# image = pyautogui.screenshot(region=(0,0, 500, 500))
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# now = strftime("%dd%mm%Yy%Hhr%Mm%Ss", gmtime()) + '.png'
# cv2.imwrite('./My Bots/now.png', image)
# now = './My Bots/' + strftime("%dd%mm%Yy%Hhr%Mm%Ss", gmtime()) + '.png'
# print(now[10:])
currenttime = strftime("%dd%mm%Yy%Hhr%Mm%Ss", gmtime())
botfilepath = '.\\My Bots\\' + currenttime + '.txt'
print(botfilepath[10:-3])