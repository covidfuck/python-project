import pygame
import random
import sys


##함수 선언 부분##
# @기능 2-5 : 매개변수로 받은 객체를 화면에 그리는 함수를 선언한다.
def paintEntity(entity, x, y):
    monitor.blit(entity, (int(x), int(y)))


# @기능 5-4 : 점수를 화면에 쓰는 함수를 선언한다.
def writeScore(score):
    myfont = pygame.font.Font('NanumGothic.ttf', 20)  # 한글 폰트
    txt = myfont.render(u'파괴한 우주괴물 수 : ' + str(score), True, (255 - r, 255 - g, 255 - b))
    monitor.blit(txt, (10, sheight - 40))


def writeGameOver():
    myfont = pygame.font.Font('NanumGothic.ttf', 40)  # 한글 폰트
    txt = myfont.render(u'우주선 폭파!! 게임 끝!', True, (255 - r, 255 - g, 255 - b))
    rect = txt.get_rect()
    rect.center = (swidth // 2), (sheight // 2)
    monitor.blit(txt, rect)
    rect1 = None
    for i in range(3, 0, -1):
        if rect1 is not None:
            monitor.fill((r, g, b), rect1)
        txt1 = myfont.render(f'{i}', True, (255 - r, 255 - g, 255 - b))
        rect1 = txt1.get_rect()
        rect1.center = (swidth // 2), (sheight // 2) + 50
        monitor.blit(txt1, rect1)
        pygame.display.update()
        pygame.time.wait(1000)
    pygame.quit()
    sys.exit()


def playGame():
    global monitor, ship, monster, missile, shipSize, currShipImageName, r, g, b

    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    # @기능 2-2 : 우주선의 초기 위치 키보드를 눌렀을 떄 이동량을 저장할 변수를 선언한다.
    shipX = swidth / 2  # 우주선 위치
    shipY = sheight * 0.8
    dx, dy = 0, 0  # 키보드를 누를 때 우주선의 이동량

    # @기능 3-2 : 우주괴물을 무작위로 추출하고 크기와 위치를 설정한다.
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size  # 우주괴물 크기
    monsterX = 0
    monsterY = random.randrange(0, int(swidth * 0.3))  # 상위 30% 위치까지만
    monsterSpeed = random.randrange(1, 5)

    # @기능 4-2 : 미사일 좌표를 초기화한다.
    missileX, missileY = None, None  # None은 미사일을 쏘지 않았다는 의미이다.

    # @기능 5-1 : 맞춘 우주괴물 수자를 저장할 변수를 선언한다.
    fireCount = 0

    # 무한반복
    while True:
        (pygame.time.Clock().tick(60))  # 게임 진행을 늦춘다(10~100 정도가 적당).
        monitor.fill((r, g, b))  # 화면 배경을 칠한다.

        # 키보드나 마우스 이벤트가 들어오는지 체크한다.
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        key_event = pygame.key.get_pressed()
                # @기능 2-3 : 방향키에 따라 우주선이 움직이게 한다.
                # 방향키를 누르면 우주선이 이동한다(누르고 있으면 계속 이동한다).
        if key_event[pygame.K_LEFT] and shipX > 0 :
            shipX -= 5 #dx = -5
        if key_event[pygame.K_RIGHT] and shipX < swidth-shipSize[0]:
            shipX += 5 # dx = +5
        if key_event[pygame.K_UP] and shipY > 0:
            shipY -= 5 # dy = -5
        if key_event[pygame.K_DOWN] and shipY < sheight-shipSize[1]:
            shipY += 5 # dy = +5
            # @기능 4-3 : 스페이스바를 누르면 미사일을 발사한다.
        if key_event[pygame.K_SPACE]:
            if missileX == None:  # 미사일을 쏜적이 없다면
                missileX = shipX + shipSize[0] / 2
                # 우주선 위치에서 미사일을 발사한다.
                missileY = shipY


        # @기능 2-4 : 우주선이 화면 안에서만 움직이게 한다.
        # if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
        #         and (0 < shipY + dy and shipY + dy <= sheight - shipSize[1]):
        #     # 화면의 중앙까지만
        #     shipX += dx
        #     shipY += dy

        paintEntity(ship, shipX, shipY)  # 우주선을 화면에 표시한다.

        # @기능 3-3 : 우주괴물이 자동으로 나타나 왼쪽에서 오른쪽으로 움직인다.
        monsterY += monsterSpeed

        # 몬스터가 우주선과 충돌했다면
        if (monsterX < shipX and shipX < monsterX + monsterSize[0]) and \
                (monsterY < shipY and shipY < monsterY + monsterSize[1]):
            writeGameOver()


        # 몬스터가 화면을 벗어났다면 다시 생성 + 점수 1점 빼기
        if monsterY > sheight:
            fireCount -= 1

            # 새로운 몬스터 생성
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size

            # x 는 랜덤
            monsterX = random.randrange(0, int(swidth))

            # y 는 꼭대기부터
            monsterY = -monsterSize[1]

            # 몬스터 속도
            monsterSpeed = random.randrange(5, 9)

        paintEntity(monster, monsterX, monsterY)
        # @기능 4-4 : 미사일을 화면에 표시한다.
        if missileX != None:  # 총알을 쏘면 좌표를 위로 변경한다.
            missileY -= 10
            if missileY < 0:
                missileX, missileY = None, None  # 총알이 사라진다.
        if missileX != None:  # 미사일을 쏜 적이 있으면 미사일을 그려준다.
            paintEntity(missile, missileX, missileY)

            # @기능 5-2 : 우주괴물이 미사일에 맞았는지 체크한다.
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                    (monsterY < missileY and missileY < monsterY + monsterSize[1]):
                fireCount += 1

                # 우주선 업그레이드
                # (방금 전 이미지와 같은 이미지가 나오지 않도록, 이전 이미지를 제외한 3개의 우주선 중 1개를 선택)
                lastShipImage = currShipImageName
                sub_list = shipImage.copy()
                sub_list.remove(lastShipImage)
                currShipImageName = random.choice(sub_list)
                ship = pygame.image.load(currShipImageName)
                shipSize = ship.get_rect().size

                # 우주괴물을 초기화한다(무작위 이미지로 다시 준비한다).
                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterY = 0
                monsterX = random.randrange(0, swidth-monsterSize[0])
                monsterSpeed = random.randrange(5, 9)

                # 미사일을 초기화한다.
                missileX, missileY = None, None  # 총알이 사라진다.

        # @기능 5-3 : 점수를 화면에 쓰는 함수를 호출한다.
        writeScore(fireCount)

        # shipX, shipY     monsterX, monsterY
        print(f'shipX : {shipX}, shipY : {shipY}')
        print(f'monsterX : {monsterX}, monsterY : {monsterY}')
        print()


        # 화면을 업데이트한다.
        pygame.display.update()


##전역 변수 선언 부분##
r, g, b = [0] * 3  # 게임 배경색
swidth, sheight = 500, 700  # 화면 크기
monitor = None  # 게임 화면
ship, shipSize = None, 0  # 우주선 객체와 크기 변수

# @기능 3-1 : 무작위로 사용할 우주괴물 이미지를 10개 준비한다.
monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', 'monster05.png', \
                'monster06.png', 'monster07.png', 'monster08.png', 'monster09.png', 'monster10.png']
shipImage = ['ship01.png', 'ship02.png', 'ship03.png', 'ship04.png']
currShipImageName = ""
monster = None  # 우주괴물
missile = None  # 미사일

if __name__ == '__main__':
    ##메인 코드 부분##
    pygame.init()
    monitor = pygame.display.set_mode((swidth, sheight))
    pygame.display.set_caption('우주괴물 무찌르기')

    # @기능 2-1 : 우주선 이미지를 준비하고 크기를 구한다.
    currShipImageName = random.choice(shipImage)
    ship = pygame.image.load(currShipImageName)
    shipSize = ship.get_rect().size

    # @기능 4-1 : 미사일 이미지를 추가한다.
    missile = pygame.image.load('missile.png')

    playGame()
