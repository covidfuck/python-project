"""

    < 파일 입/출력 >

    변수 = open("파일명" , "열기모드")

    1. open()
        : 파일 열기!
        : 파일명 - '파일 경로 + 파일명 + 확장자'로 구성된 1개의 str형
                   파일 경로 공백시 기본 경로 : 소스파일(.py)이 위치한 디렉토리
                   경로 구분자는 '/' 혹ㅇㄴ '\\'로 표기한다.

        : 열기모드
            'w' : write 쓰기모드 (덮어씀)
            'r' : read 읽기모드
            'a' : append 추가모드 (추가함)

        : 파일을 객체로 포장하여 return 한다.

    2. write()
        - write('문자열')
        - writelines(리스트)

    3. read()
        - read() : 처음 줄 ~ 마지막 줄 모두 잃고, 이를 1개의 str형으로 return
        - readline() : 현재 위치에서 1줄만 읽어 return
        - readlines() : 각 줄을 리스트에 하나씩 담아 return

    4. close()
        - 파일 저장 및 닫기
        - 안하면 '메모리 누수'가 발생할 수 있음
        - open()을 했다면 반드시 close()를 하자!


"""
f = open("aa.txt", "w", encoding= 'utf-8')
f.write('Iphone good\n')
f.write('Hello Python\n')
f.write('ABC DEF ~~~\n')
f.write("안녕하세요\n")
f.close()

f = open("aa.txt", "a")
f.write('add text\n')
f.close()

f = open("aa.txt", "r", encoding= 'utf-8')
a = f.read()
print(a)

print('파일 저장 완료!')

