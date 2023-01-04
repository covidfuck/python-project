import pygame
import sys  # sys.exit() <-- 프로그램 종료
import random

# 창의 가로, 세로
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 색상 (tuple, RGB) # 구글에 컬러피커 검색
hero_color = (255, 255, 255)
enemy_color = (224, 18, 18)
black = (0, 0, 0)

# pygame 초기화
pygame.init()

# 창 제목
pygame.display.set_caption("GAME!")

# 화면 세팅
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 캐릭터(원)의 위치
pos_x = SCREEN_WIDTH / 2
pos_y = SCREEN_HEIGHT / 2

enemy_x = random.randrange(0, 640)
enemy_y = random.randrange(0, 480)

clock = pygame.time.Clock()

score = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 4
    if key_event[pygame.K_RIGHT]:
        pos_x += 4
    if key_event[pygame.K_UP]:
        pos_y -= 4
    if key_event[pygame.K_DOWN]:
        pos_y += 4

    screen.fill(black)
    hero_circle = pygame.draw.circle(screen, hero_color, (pos_x, pos_y), 15)
    enemy_circle = pygame.draw.circle(screen, enemy_color, (enemy_x, enemy_y), 15)
    pygame.display.update()

    if(hero_circle.colliderect(enemy_circle)):
        print("+10")
        score += 10
        print(f'총점 : {score}')
        enemy_x = random.randrange(5, 635)
        enemy_y = random.randrange(5, 475)

# 1. 사용자가 enemu_circle 에 닿으면, 점수를 10점 추가한 뒤
#    ebemy_circle 을 다른 위치에 생성시킨다. (random.randrange() 사용)

# 2. enemy_circle이 5개 만들어지도록 한다. 랜덤하게 움직이도록 한다. 속도도 랜덤하게..
#       선택 1) 벽에 부딪히면 각도, 방향 바꿈
#       선택 2) 사용자를 따라가도록 한다.