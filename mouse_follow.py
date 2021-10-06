import pyautogui
import easygui
import time
import os

title = "Mouse Follower"
msg = "Select your mouse recorder file:"
choices = []
count_files = len(os.listdir('My Bots/'))
for i in range (0, count_files):
    if(os.listdir('My Bots/')[i][-4:] == '.txt'):
        choices.append(os.listdir('My Bots/')[i])
choice = easygui.choicebox(msg, title, choices)
file_path ='My Bots\\' + choice
with open(file_path, 'r') as fin:
        clicks = fin.read().splitlines(True)

file = open(file_path, "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

for n in range (0, line_count):
    scan_line = clicks[n]
    first_line = scan_line[:-1].rsplit(' ', 2)
    click_type = first_line[0]
    click_x = int(first_line[1])
    click_y = int(first_line[2])

    if click_type == "click":
        pyautogui.click(click_x, click_y)
    elif click_type == "double_click":
        pyautogui.doubleClick(click_x, click_y)
    elif click_type == "right_click":
        pyautogui.rightClick(click_x, click_y)
    elif click_type == "sleep_time":
        time.sleep(click_x)

msg = 'Script ended successfully.'
easygui.msgbox(msg, title)