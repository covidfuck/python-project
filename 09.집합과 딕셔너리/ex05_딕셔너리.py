"""

    ditionary : {키:값, 키:값, 키:값, .....}
        - 키 : 보통 문자열 혹은 정수
        - 값 : 키와 연결(mapping)된 값
        - 값에 이름(별명)을 붙여주는 구조
        - 딕셔너리는 '키-값' 쌍을 원소라 한다.
        - 한 딕셔너리에 '키'는 중복 X, '값'은 중복 O
        - '인덱스' 대신 '키'를 사용한다.

"""
info = {'name' : '홍길동', 'age' : 10, 'height' : 143.5, 'tel' : '010-1111-2222'}
print(info['age'])
print(info)
info['height'] = 150.2
print(info)
info['address'] = '서울시 마포구 노고산동'
print(info)
