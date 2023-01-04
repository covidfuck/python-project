"""
    1. 사용자가 'exit'을 입력 할 때까지 영단어와 그의 뜻을 계속 입력 받는다.
        - exit를 입력하면
        입력 받았던 모든 영단어, 뜻을 'my_word.xlsx'에 저장
"""
import openpyxl

wb = openpyxl.Workbook()

ws = wb.active # 기본 시트 생성

while True:
    a = input("영단어를 입력하세요(종료는 exit) : ")
    if a == 'exit':
        break
    else:
        mean = input("단어의 뜻을 입력하세요 : ")
        ws.append([f'{a}', f'{mean}'])

wb.save('quiz.xlsx')