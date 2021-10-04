import pyautogui
import easygui
import time

with open('mouse_rec.txt', 'r') as fin:
        clicks = fin.read().splitlines(True)

file = open("mouse_rec.txt", "r")
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
    elif click_type == "sleep_time":
        time.sleep(click_x)

title = "Mouse Follower"
msg = 'Script ended successfully.'
easygui.msgbox(msg, title)