"""
    Student 클래스
    필드 (변수) : 이름(name), 국(ko), 영,(en), 수(ma)
                 평균(avg), 등급(grade)

    메서드 (함수) :
        1) set_data()
            인자 : X
            하는 일 : 이름, 국, 영, 수를 input()으로 입력 받고 필드에 저장
                     평균, 등급은 계산되어 저장
                     (90 이상 : A등급)
                     (80 이상 90 미만 : B등급)
                     ...
                     (60 미만 : F등급)
            리턴 : x
        2) print_data()
            인자 : x
            하는 일 : 필드의 모든 정보를 print()로 출력
            리턴 : x
        ==> Student 객체 3개를 만들어서 3학생의 모든 정보를 저장 및 출력
            (set_data(), print_data() 활용)
"""
class Student:
    name = ""
    ko = 0
    en = 0
    ma = 0
    avg = 0
    grade = ""
    def set_data(self):
        self.name = input("이름 : ")
        self.ko = int(input("국어 점수 : "))
        if self.ko > 100:
            print("100점 이하의 점수를 입력해주세요!!")
            self.ko = int(input("국어 점수 : "))
        self.en = int(input("영어 점수 : "))
        if self.en > 100:
            print("100점 이하의 점수를 입력해주세요!!")
            self.en = int(input("영어 점수 : "))
        self.ma = int(input("수학 점수 : "))
        if self.ma > 100:
            print("100점 이하의 점수를 입력해주세요!!")
            self.ma = int(input("수학 점수 : "))
        self.avg = float((self.ko + self.en + self.ma) / 3)
        if self.avg >= 90:
            self.grade = "A"
        elif 80 <= self.avg < 90:
            self.grade = "B"
        elif 70 <= self.avg < 80:
            self.grade = "C"
        elif 60 <= self.avg < 70:
            self.grade = "D"
        else:
            self.grade = "F"
    def print_data(self):
            print(f'이름 : {self.name}\n국어 : {self.ko}  수학 : {self.ma}  영어 : {self.en}')
            print(f'평균 : {self.avg}  등급 : {self.grade}!!')

s = [Student(), Student(), Student()]

for i in range(3):
    s[i].set_data()
    s[i].print_data()


