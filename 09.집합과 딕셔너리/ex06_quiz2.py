"""

    [영단어 프로그램]
    메뉴)
        1. 단어 추가
        2. 단어 검색
        3. 단어 수정
        0. 종료 하기

    1. 단어 추가 :
        영단어, 그의 뜻을 각각 입력 받고,
        단어장 (wordbook)에 해당 단어를 추가한다.
        키 : 영단어
        값 : 그의 뜻
    2. 단어 검색 :
        영단어를 입력 받고 그 단어가 있는지 검색 ('in' 활용)
        있으면 - 그의 '뜻' 출력
        없으면 - '미등록 단어' 출력
    3. 단어 수정 :
        수정할 영단어를 입력 받고 그 단어의 뜻을 입력 받아서
        새 뜻으로 수정
        없으면 - '미등록 단어' 출력
    4. 단어장 보기
    5. 퀴즈
        랜덤하게 단어를 1개 선택한다. (컴퓨터가)
        '뜻'을 문제로 낸다.
        사용자는 그 단어를 입력한다.
        맞으면 정답!, 틀리면 땡!
    wordbook = {}
    wordbook['apple'] = '사과'

"""
import random
wordbook = {}

menu = "1. 단어 추가\n2. 단어 검색\n3. 단어 수정\n4. 단어장 보기\n5. 퀴즈\n0. 종료\n입력 : "

print("---------------------------- 영어 단어장 관리하기 ----------------------------")
while True:
    select = input(menu)
    if select == '1':
        word = input('추가할 단어를 입력해 주세요 : ')
        mean = input(f'{word}의 뜻을 입력해 주세요 : ')
        if word in wordbook:
            print("이미 있는 단어 입니다.")
        else:
            wordbook[word] = mean
    if select == '2':
        word = input("검색할 단어를 입력해 주세요 : ")
        if word in wordbook:
            print(wordbook[word])
        else:
            print("미등록 단어 입니다.")
    if select == '3':
        word = input("수정할 단어를 입력해 주세요 : ")
        mean = input("수정할 단어의 뜻을 입력해 주세요 : ")
        if word in wordbook:
            wordbook[word] = mean
        else:
            print("미등록 단어 입니다.")
    if select == '4':
        for k in wordbook:
            print(f'{k} : {wordbook[k]}')
            print(wordbook)
    if select == '5':
        print('-------------------- QUIZ --------------------')
        quiz = list(wordbook)
        a = random.choice(quiz)
        print(f'{wordbook[a]}(은)는 영어로?')
        b = input("단어를 입력해 주세요 : ")
        if a == b:
            print("정답입니다!")
        else:
            print("틀렸습니다!")
    if select == '0':
        break
    else:
        continue

words = list(wordbook)
print(words, type(words))
print(random.choice(words))