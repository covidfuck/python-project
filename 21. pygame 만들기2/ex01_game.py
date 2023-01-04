import pygame
import random
import sys

sWidth = 640
sHeight = 480
r, g, b = 0, 0, 0
ship = None
shipSize = 0
monster = None
missile = None

pygame.init()
monitor = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption("Shoot Monster!")

ship = pygame.image.load('ship01.png')


# 매개변수로 받은 entity를 화면에 그리는 함수
def paintEntity(entity, x, y):
    monitor.blit(entity, (int(x), int(y)))

# 현재 점수를 화면에 그려주는 함수
def writeScore(score):
    myFont = pygame.font.SysFont('arial', 20, bold = True, italic = False)
    txt = myFont.render(u'파괴한 우주괴물 수 : ' + str(score),
                        True,
                        (255-r, 255-g, 255-b) # 배경색의 반전색 사용
    )
    monitor.blit(txt, (10, sHeight-40))

def SetMonster():
    global monster, monsterSize, monsterX, monsterY, monsterSpeed
    monsterImage = [
        'monster01.png', 'monster02.png', 'monster03.png',
        'monster04.png', 'monster05.png', 'monster06.png',
        'monster07.png', 'monster08.png', 'monster09.png',
        'monster10.png',
    ]
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size
    monsterX = 0
    monsterY = random.randrange(int(sHeight * 0.3))
    monsterSpeed = random.randint(1, 5)

# 게임 시작 함수
def playGame():
    global monitor, ship, monster, missile
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    shipX = sWidth * .5 # 우주선 위치
    shipY = sHeight * .8

    dx = 0
    dy = 0

    # 맞춘 우주괴물 숫자
    fireCount = 0

    while True:
        pygame.time.Clock().tick(60)
        monitor.fill = ((r, g, b))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            dx -= 4
        if key_event[pygame.K_RIGHT]:
            dx += 4
        if key_event[pygame.K_UP]:
            dy -= 4
        if key_event[pygame.K_DOWN]:
            dy += 4
        if key_event[pygame.K_SPACE]: # 미사일 쏘기
            pass

        monsterX += monsterSpeed
        if monsterX > sWidth:
            SetMonster()

        pygame.display.update()
