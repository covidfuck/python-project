import pyautogui

# 마우스 자동 컨트롤

pyautogui.move(0, 100) # move(x, y) : 상대 좌표
pyautogui.move(100, 100, duration = 1) # 1초 동안 이동

pyautogui.moveTo(2000, 0, duration=1) # 절대 좌표

# 현재 커서의 좌표 구하기
pyautogui.sleep(3)
p = pyautogui.position()
print(p)