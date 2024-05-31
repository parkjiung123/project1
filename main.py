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