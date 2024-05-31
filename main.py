import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH= 900
HEIGHT= 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

THROW_SNOW_BALL_SOUND = pygame.mixer.Sound('Source/Throw_Snowball.mp3')
HIT_SNOW_BALL_SOUND=pygame.mixer.Sound('Source/Hit_Snowball.mp3')

HP_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

FPS = 60
SPEED = 5
SNOWBALL_SPEED = 7
MAX_SNOWBALL = 2
CHARACTER_WIDTH = 55
CHARACTER_HEIGHT = 40

BOY_HIT = pygame.USEREVENT + 1
GIRL_HIT = pygame.USEREVENT + 2

BOY_IMAGE = pygame.image.load(
    os.path.join('Source','Boy.png'))
BOY = pygame.transform.scale(
    BOY_IMAGE,(BOY,CHARACTER_WIDTH,CHARACTER_HEIGHT))
GIRL_IMAGE = pygame.image.load(
    os.path.join('Source','Girl.png'))
GIRL = pygame.transform.scale(
    GIRL_IMAGE,(GIRL,CHARACTER_WIDTH,CHARACTER_HEIGHT))

BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join('Source','Background.jpg')),(WIDTH,HEIGHT))

def draw_display(girl,boy,girl_snowball,boy_snowball,girl_hp,boy_hp):
    WIN.blit(BACKGROUND,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    girl_hp_text=HP_FONT.render("HP: " + str(girl_hp),1,WHITE)
    boy_hp_text=HP_FONT.render("HP: "+ str(boy_hp),1,WHITE)
    WIN.blit(girl_hp_text,(WIDTH-girl_hp_text.getwidth()-10,10))
    WIN.blit(boy_hp_text,(10,10))

    WIN.blit(BOY,(boy.x,boy.y))
    WIN.blit(GIRL,(girl.x,girl.y))

    for snowball in girl_snowball:
        pygame.draw.rect(WIN,RED, snowball)

    for snowball in boy_snowball:
        pygame.draw.rect(WIN, YELLOW,snowball)

    pygame.display.update()

def boy_handle_movement(keys_pressed,boy):
    if keys_pressed[pygame.K_a] and boy.x - SPEED > 0:
        boy.x -= SPEED
    if keys_pressed[pygame.K_d] and boy.x + SPEED + boy.width < BORDER.x:
        boy.x += SPEED
    if keys_pressed[pygame.K_w] and boy.y - SPEED > 0:
        boy.y -= SPEED
    if keys_pressed[pygame.K_s] and boy.y + SPEED + boy.height < HEIGHT - 15:
        boy.y += SPEED

def girl_handle_movement(keys_pressed,girl):
    if keys_pressed[pygame.K_LEFT] and girl.x - SPEED > BORDER.x + BORDER.width:
        girl.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and girl.x + SPEED + girl.width < WIDTH:
        girl.x += SPEED
    if keys_pressed[pygame.K_UP] and girl.y - SPEED > 0:
        girl.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and girl.y + SPEED + girl.height < HEIGHT - 15:
        girl.y += SPEED

def handle_snowball(boy_snowball,girl_snowball,boy,girl):
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
        elif snowball.x <0:
            girl_snowball.remove(snowball)
