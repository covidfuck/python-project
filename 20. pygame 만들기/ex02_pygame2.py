"""

ex01_pygame
    사용자가 enemu_circle 에 닿으면, 점수를 10점 추가한 뒤
    ebemy_circle 을 다른 위치에 생성시킨다. (random.randrange() 사용)

ex02_pygame2
    enemy_circle이 5개 만들어지도록 한다. 랜덤하게 움직이도록 한다. 속도도 랜덤하게..
      선택 1) 벽에 부딪히면 각도, 방향 바꿈
      선택 2) 사용자를 따라가도록 한다.

"""
import pygame
import sys  # sys.exit() <-- 프로그램 종료
import random

class EnemyCircle:

    def __init__(self, pos_x=0, pos_y=0, dir_x=1, dir_y=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.r = random.randrange(10, 30)
# 창의 가로, 세로
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 색상 (tuple, RGB) # 구글에 컬러피커 검색
hero_color = (255, 255, 255) # 흰색
enemy_color = (224, 18, 18) # 빨간색
black = (0, 0, 0) # 검정색

# pygame 초기화
pygame.init()

# 창 제목
pygame.display.set_caption("GAME!")

# 화면 세팅
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 캐릭터(원)의 위치
hero_x = SCREEN_WIDTH / 2
hero_y = SCREEN_HEIGHT / 2

clock = pygame.time.Clock()

circles = [
    EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)),
    EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)),
    EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)),
    EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)),
    EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)),
]


start_tick = pygame.time.get_ticks() # 시작 시간 저장

circle_size = []

while True:
    seconds = (pygame.time.get_ticks() - start_tick) / 1000
    print(seconds)
    clock.tick(60)

    if seconds // 5 > len(circles) - 5:
        print("공 추가")
        circles.append(EnemyCircle(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    for circle in circles:
        if circle.pos_x < 0 and circle.dir_x == -1:
            circle.dir_x = 1
        if circle.pos_x > 640 and circle.dir_x == 1:
            circle.dir_x = -1
        if circle.pos_y < 0 and circle.dir_y == -1:
            circle.dir_y = 1
        if circle.pos_y > 480 and circle.dir_y == 1:
            circle.dir_y = -1

        circle.pos_x += 2 * circle.dir_x
        circle.pos_y += 2 * circle.dir_y

        enemy = pygame.draw.circle(screen, enemy_color, (circle.pos_x, circle.pos_y), circle.r)

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        hero_x -= 5
    if key_event[pygame.K_RIGHT]:
        hero_x += 5
    if key_event[pygame.K_UP]:
        hero_y -= 5
    if key_event[pygame.K_DOWN]:
        hero_y += 5

    hero_circle = pygame.draw.circle(screen, hero_color, (hero_x, hero_y), 15)
    pygame.display.update()

    if hero_circle.colliderect(enemy):
        print("충돌")
        sys.exit()




