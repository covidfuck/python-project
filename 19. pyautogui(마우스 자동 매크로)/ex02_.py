# import pyautogui

# pyautogui.sleep(3)
# p = pyautogui.position()
# print(p) # (x=468, y=16)
# pyautogui.click(x=468, y=16) # help 클릭

"""
pyautogui.click(x, y) <-- 클릭
pyautogui.doubleClick(x, y) <-- 더블클릭
pyautogui.mouseDown()
pyautogui.mouseUp()
"""
import pyautogui

# pyautogui.mouseInfo()

pyautogui.sleep(3)
pyautogui.click(x=466, y=345)
pyautogui.mouseDown()
pyautogui.move(200, 0)
pyautogui.move(0, 200)
pyautogui.move(-200, 0)
pyautogui.move(0, -200)
pyautogui.mouseUp()

# pyautogui.sleep(3)
# p = pyautogui.position()
# print(p)
# pyautogui.click(607, 329)
# pyautogui._mouseMoveDrag('2', 607, 529)

