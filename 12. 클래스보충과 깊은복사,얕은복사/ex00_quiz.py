"""
    Student 클래스
    필드 (변수) : 이름(name), 국(ko), 영(en), 수(ma)
                 평균(avg), 등급(grade)

    메서드 (함수) :
        1) set_data()
            인자 : X
            하는 일 : 이름, 국, 영, 수를 input()으로 입력 받고 필드에 저장
                     평균, 등급은 계산되어 저장
                     (90 이상 : A 등급)
                     (80 이상 ~ 90 미만 : B 등급)
                     ...
                     (60 미만 : F 등급)
            리턴 : X
        2) print_data()
            인자 : X
            하는 일 : 필드의 모든 정보를 print()로 출력
            리턴 : X
    => Student 객체 3개를 만들어서 3학생의 모든 정보를 저장 및 출력
        (set_data(), print_data() 활용)
"""
class Student:
    name = ''
    ko = 0
    en = 0
    ma = 0
    avg = 0.0
    grade = 'F'

    def set_data(self):

        # 이름 입력 받기
        self.name = input('이름 : ')

        # 세 점수 입력 받기
        self.ko = int(input('국 : '))
        self.en = int(input('영 : '))
        self.ma = int(input('수 : '))

        # 평균 구하기
        self.avg = (self.ko + self.en + self.ma) / 3

        self.calc_grade()

    def calc_grade(self):
        # 학점 구하기
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        elif self.avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def print_data(self):
        print('==== 학생 정보 ====')
        print(f'이름 : {self.name}')
        print(f'국/영/수 : {self.ko}/{self.en}/{self.ma}')
        print(f'평균 : {self.avg:.2f}점')
        print(f'학점 : {self.grade}')


students = [Student(), Student(), Student()]
for i in range(3):
    students[i].set_data()


for i in range(3):
    students[i].print_data()









