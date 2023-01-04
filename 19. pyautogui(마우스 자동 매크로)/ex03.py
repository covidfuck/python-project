import pyautogui
"""
    이미지 찾기
    
pyautogui.sleep(3)
a = pyautogui.locateOnScreen("a.png")
print(a)

pyautogui.click(a, duration=1)
"""

# 모든 체크박스 클릭하기
import pyautogui

pyautogui.sleep(3)
for i in pyautogui.locateAllOnScreen("check.png", confidence = 0.7):
    pyautogui.click(i)
