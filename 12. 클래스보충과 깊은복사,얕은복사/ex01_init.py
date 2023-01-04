"""
    1. 클래스 + () ==> 클래스 모양대로 객체를 생성한다.
                   그 클래스의 __init__()이라는 함수가 자동으로 실행된다.

    2. __init__() 이란?
        - 생성자 (constructor)
        - 객체 생성 시 필요한 작업을 적어두는 메서드


"""

# class Book:
#     title = ''
#     author = ''
#
#     def __init__(self):
#         print('책 생성됨!')

class Book:
    title = ''
    author = ''

    def __init__(self, t, a):
        print('책 생성됨!')
        self.title = t
        self.author = a

    def print_info(self):
        print(f'제목 : {self.title}')
        print(f'저자 : {self.author}')

a = Book('해리포터와 마법사의 돌', 'JK 롤링')
b = Book('책제목..', '홍길동')
c = Book('책2 제목..', '고길동')
a.print_info()
b.print_info()
c.print_info()

a.title = '해리포터와 마법사의 돌2'
a.author = 'JK 롤링3'
b.title = '책제목4..'
b.author = '홍길동5'

a.print_info()
b.print_info()
c.print_info()