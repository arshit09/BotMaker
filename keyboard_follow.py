from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

temp = "Whats Up?"

for char in temp:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.05)