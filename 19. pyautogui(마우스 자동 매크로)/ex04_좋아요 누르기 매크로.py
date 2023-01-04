"""

    scroll : pyautogui.scroll(100)

"""
import pyautogui

pyautogui.sleep(4)
for j in range(10):
    pyautogui.scroll(300)
    pyautogui.sleep(2)
    for i in pyautogui.locateAllOnScreen("unlike.png"):
        pyautogui.click(i, duration=0.5)
