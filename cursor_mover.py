import pyautogui
import time
import random
from win32api import GetSystemMetrics

minutes = float(input("Set duration: "))
seconds = minutes * 60

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

while seconds != 0:
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    print(f"{x}, {y}")

    time.sleep(1)

    if seconds % 10 == 0.:
        pyautogui.press("esc")
        pyautogui.moveTo(x, y)

    print(seconds)
    seconds -= 1
    if seconds == 0:
        print("Timer stopped. Let's work!!")
        exit(0)
