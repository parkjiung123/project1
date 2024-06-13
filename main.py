import pygame
import os, sys
import random

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowball Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
############### PHASE 2 ###############   시작화면 구성을 위한 색 추가
SKYBLUE = (153, 255, 255)        

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

THROW_SNOW_BALL_SOUND = pygame.mixer.Sound('Source/Throw_Snowball.mp3')
HIT_SNOW_BALL_SOUND = pygame.mixer.Sound('Source/Hit_Snowball.mp3')

HP_FONT = pygame.font.SysFont('comicsans', 40)
############### PHASE 2 ###############    시작 화면 및 종료를 위한 폰트 추가
WINNER_FONT = pygame.font.SysFont('comicsans', 50)
GAMEOVER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60
SPEED = 5
SNOWBALL_SPEED = 7
MAX_SNOWBALL = 2
CHARACTER_WIDTH = 60
CHARACTER_HEIGHT = 50

############### PHASE 2 ###############    시작 및 재시작 구분 위한 전역변수선언
winner_text=""
STATUS=1

BOY_HIT = pygame.USEREVENT + 1
GIRL_HIT = pygame.USEREVENT + 2

BOY_IMAGE = pygame.image.load(
    os.path.join('Source', 'Boy.png'))
BOY = pygame.transform.scale(
    BOY_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
GIRL_IMAGE = pygame.image.load(
    os.path.join('Source', 'Girl.png'))
GIRL = pygame.transform.scale(
    GIRL_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Source', 'Background.jpg')), (WIDTH, HEIGHT))

SNOWBALL_IMAGE = pygame.image.load(os.path.join('Source', 'Snowball.png'))
SNOWBALL = pygame.transform.scale(SNOWBALL_IMAGE, (20, 20))

PENGUIN_IMAGE = pygame.image.load(os.path.join('Source', 'Penguin.png'))
PENGUIN = pygame.transform.scale(PENGUIN_IMAGE, (55, 45))


class Penguin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

    def draw(self):
        WIN.blit(PENGUIN, (self.x, self.y))
        self.y += 1


def draw_display(girl, boy, girl_snowball, boy_snowball, penguins, girl_hp, boy_hp):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    girl_hp_text = HP_FONT.render("HP: " + str(girl_hp), 1, BLACK)
    boy_hp_text = HP_FONT.render("HP: " + str(boy_hp), 1, BLACK)
    WIN.blit(girl_hp_text, (WIDTH - girl_hp_text.get_width() - 10, 10))
    WIN.blit(boy_hp_text, (10, 10))

    WIN.blit(BOY, (boy.x, boy.y))
    WIN.blit(GIRL, (girl.x, girl.y))

    for snowball in girl_snowball:
        WIN.blit(SNOWBALL, (snowball.x, snowball.y))

    for snowball in boy_snowball:
        WIN.blit(SNOWBALL, (snowball.x, snowball.y))

    for penguin in penguins:
        penguin.draw()

    pygame.display.update()


def boy_handle_movement(keys_pressed, boy):
    if keys_pressed[pygame.K_a] and boy.x - SPEED > 0:
        boy.x -= SPEED
    if keys_pressed[pygame.K_d] and boy.x + SPEED + boy.width < BORDER.x:
        boy.x += SPEED
    if keys_pressed[pygame.K_w] and boy.y - SPEED > 0:
        boy.y -= SPEED
    if keys_pressed[pygame.K_s] and boy.y + SPEED + boy.height < HEIGHT - 15:
        boy.y += SPEED


def girl_handle_movement(keys_pressed, girl):
    if keys_pressed[pygame.K_LEFT] and girl.x - SPEED > BORDER.x + BORDER.width:
        girl.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and girl.x + SPEED + girl.width < WIDTH:
        girl.x += SPEED
    if keys_pressed[pygame.K_UP] and girl.y - SPEED > 0:
        girl.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and girl.y + SPEED + girl.height < HEIGHT - 15:
        girl.y += SPEED


def handle_snowball(boy_snowball, girl_snowball, boy, girl, penguins):
    for snowball in boy_snowball:
        snowball.x += SNOWBALL_SPEED
        if girl.colliderect(snowball):
            pygame.event.post(pygame.event.Event(GIRL_HIT))
            boy_snowball.remove(snowball)
        elif snowball.x > WIDTH:
            boy_snowball.remove(snowball)

    for snowball in girl_snowball:
        snowball.x -= SNOWBALL_SPEED
        if boy.colliderect(snowball):
            pygame.event.post(pygame.event.Event(BOY_HIT))
            girl_snowball.remove(snowball)
        elif snowball.x < 0:
            girl_snowball.remove(snowball)

    penguins_to_remove = []
    snowballs_to_remove = []

    for penguin in penguins:
        for snowball in boy_snowball + girl_snowball:
            if penguin.x < snowball.x < penguin.x + penguin.width and penguin.y < snowball.y < penguin.y + penguin.height:
                penguins_to_remove.append(penguin)
                snowballs_to_remove.append(snowball)
                HIT_SNOW_BALL_SOUND.play()

    for penguin in penguins_to_remove:
        if penguin in penguins:
            penguins.remove(penguin)

    for snowball in snowballs_to_remove:
        if snowball in boy_snowball:
            boy_snowball.remove(snowball)
        if snowball in girl_snowball:
            girl_snowball.remove(snowball)

    for penguin in penguins:
        if penguin.y > HEIGHT:
            penguins.remove(penguin)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()


def runGame():
    ############### PHASE 2 ############### 게임오버 시 승리 확인 하기위한 변수
    global winner_text, STATUS
    STATUS = 2
    
    girl = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    boy = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    girl_snowball = []
    boy_snowball = []
    penguins = [Penguin(random.randint(0, WIDTH - 30), 0) for _ in range(5)]

    girl_hp = 10
    boy_hp = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ############### PHASE 2 ###############
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and len(boy_snowball) < MAX_SNOWBALL:
                    snowball = pygame.Rect(
                        boy.x + boy.width, boy.y + boy.height // 2 - 2, 10, 5)
                    boy_snowball.append(snowball)
                    THROW_SNOW_BALL_SOUND.play()

                if event.key == pygame.K_SLASH and len(girl_snowball) < MAX_SNOWBALL:
                    snowball = pygame.Rect(
                        girl.x, girl.y + girl.height // 2 - 2, 10, 5)
                    girl_snowball.append(snowball)
                    THROW_SNOW_BALL_SOUND.play()

            if event.type == GIRL_HIT:
                girl_hp -= 1
                HIT_SNOW_BALL_SOUND.play()

            if event.type == BOY_HIT:
                boy_hp -= 1
                HIT_SNOW_BALL_SOUND.play()

        winner_text = ""
        if girl_hp <= 0:
            winner_text = "Boy Wins!"

        if boy_hp <= 0:
            winner_text = "Girl Wins!"

        if winner_text != "":
            ############### PHASE 2 ###############
            run = False

        keys_pressed = pygame.key.get_pressed()
        boy_handle_movement(keys_pressed, boy)
        girl_handle_movement(keys_pressed, girl)

        handle_snowball(boy_snowball, girl_snowball, boy, girl, penguins)
        draw_display(girl, boy, girl_snowball, boy_snowball, penguins, girl_hp, boy_hp)

        if random.randint(0, 200) == 0: 
            penguins.append(Penguin(random.randint(0, WIDTH - 30), 0))


#######################################
############### PHASE 2 ###############
#######################################

#게임 시작화면을 보여주는 showStartScreen 함수
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 50)
    titleSurf1 = titleFont.render('Snowball Game!', True, WHITE, SKYBLUE)
    titleSurf2 = titleFont.render('Snowball Game!', True, BLACK)
    pressKeySurf = HP_FONT.render('Press any key to start.', True, BLACK)

    degrees1 = 0
    while True:
        WIN.blit(BACKGROUND, (0, 0))
        
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WIDTH / 2, HEIGHT / 2)
        WIN.blit(rotatedSurf1, rotatedRect1)

        titleRect2 = titleSurf2.get_rect()
        titleRect2.center = (WIDTH / 2, HEIGHT / 2)
        WIN.blit(titleSurf2, titleRect2)

        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WIDTH / 2 - pressKeyRect.width / 2, HEIGHT - 60)
        WIN.blit(pressKeySurf, pressKeyRect)

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        degrees1 += 1


#키 누르는 것을 체크하는 checkForKeyPress 함수
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
                terminate()
            return True
    return False


#게임 종료시 승리자를 표시하고 재시작 안내 문구를 알리는 showGameOver함수
def showGameOver():
    gameOverSurf = GAMEOVER_FONT.render('Game Over', True, BLACK)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (WIDTH / 2, 50)

    pressKeySurf = HP_FONT.render('Press any key to restart.', True, BLACK)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WIDTH / 2 - pressKeyRect.width / 2, HEIGHT - 60)
    
    while True:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(gameOverSurf, gameOverRect)
        WIN.blit(pressKeySurf, pressKeyRect)
        draw_winner(winner_text)
        

        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

#게임 종료시 작동되는 terminate 함수
def terminate():
    pygame.quit()
    sys.exit()

# 여러번 진행할 수 있도록 구성된 main 함수
def main():
    showStartScreen()
    while True:
        runGame()
        showGameOver()

#######################################
############### PHASE 2 ###############
#######################################



if __name__ == "__main__":
    main()
