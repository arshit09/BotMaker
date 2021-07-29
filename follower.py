import pyautogui
import time

with open('tracker.txt', 'r') as fin:
        clicks = fin.read().splitlines(True)

file = open("tracker.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

i = 0
while i < line_count:
    scan_line = clicks[i]
    first_line = scan_line[:-1].rsplit(' ', 2)
    click_type = scan_line[:-1].rsplit(' ', 2)[0]
    click_x = scan_line[:-1].rsplit(' ', 2)[1]
    click_y = scan_line[:-1].rsplit(' ', 2)[2]

    if click_type == "click":
        pyautogui.click(int(click_x), int(click_y))
        time.sleep(0.5)
    elif click_type == "double_click":
        pyautogui.doubleClick(int(click_x), int(click_y))
        time.sleep(0.5)

    i += 1