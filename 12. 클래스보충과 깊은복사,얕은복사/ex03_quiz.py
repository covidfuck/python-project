"""
    Pokemon 클래스 만들기
        - 필드 : 이름, 레벨, 체력(hp), 공격력(ap)
        - 메서드 :
            1) __init__()
            2) __str__()
            3) level_up()
        +   4) attack()
"""
class Pokemon:
    name = ''
    level = 0
    hp = 0
    ap = 0

    def __init__(self, name, level, hp=-1, ap=-1):
        self.name = name
        self.level = level
        if hp == -1:
            self.hp = self.level * 100
        else:
            self.hp = hp

        if ap == -1:
            self.ap = self.level * 5
        else:
            self.ap = ap

    def __str__(self):
        return f'{self.name}, Lv.{self.level}, Hp.{self.hp}, Ap.{self.ap}'

    def level_up(self):
        self.level += 1
        self.hp += 100
        self.ap += 5

    def attack(self, enemy):
        print(f'{self.name}(이)가 {enemy.name}(을)를 공격!')
        enemy.hp -= self.ap
        if enemy.hp <= 0:
            print(f'상대방 {enemy.name}(을)를 물리쳤다!')
        else:
            print(f'상대방 {enemy.name}의 남은 체력 : {enemy.hp}')

p1 = Pokemon('피카츄', 1)
p2 = Pokemon('피카츄', 5)
print(p1)  # p1.__str__()
print(p2)  # p2.__str__()

p1.attack(p2)  # p1이 p2를 공격.. p2의 체력은 p1의 공격력만큼 감소
p2.attack(p1)  # p2가 p1을 공격.. p1의 체력은 p2의 공격력만큼 감소


