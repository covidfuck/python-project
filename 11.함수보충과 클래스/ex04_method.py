"""
    메서드(method) : 클래스 안에 정의된 함수
                    객체의 행동하는 방식

"""
class poketmon:
    name = ''
    level = 0
    hp = 0
    def level_up(self):
        print(f'{self.name} 레벨업!!!')
        self.level += 1
        self.hp += 100

p1 = poketmon()
p2 = poketmon()

p1.name = "피카츄"
p1.level = 15
p1.hp = 1000

p2.name = "꼬부기"
p2.level = 20
p2.hp = 2000

print(f'이름 : {p1.name}  레벨 : {p1.level}  체력 : {p1.hp}')
print(f'이름 : {p2.name}  레벨 : {p2.level}  체력 : {p2.hp}')

p1.level_up()
p2.level_up()

print(f'이름 : {p1.name}  레벨 : {p1.level}  체력 : {p1.hp}')
print(f'이름 : {p2.name}  레벨 : {p2.level}  체력 : {p2.hp}')