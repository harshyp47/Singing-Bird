#Singing Bird, Python Project, Semester II...- - ->>> Created by: Sandhya Chettiar and Harsh Parmar

import pygame
from random import randint
import time, audioop
import pyaudio
SAMPLErate = 48000
TIMEdivlx = [0.2, 0.5, 1.0,2.0,5.0,10.0]
TIMEdiv = 0

CHUNK = int( float(SAMPLErate) * TIMEdivlx[TIMEdiv])
FORMAT = pyaudio.paInt16
CHANNELS =  1 #for no. of input channels
RATE = 88200

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, rate=RATE,input=True, frames_per_buffer = CHUNK, channels = CHANNELS)

green = (35, 232, 61)
blue = (37, 241, 245)
black = (0, 0, 0)
grey = (9, 105, 16)
grey2 = (24, 168, 33)
grey3 = (220, 220, 220)
green2 = (161, 255, 167)
green3 = (87, 255, 98)
yellow = (246, 255, 0)
white = (255, 255, 255)
orange = (255, 187, 0)
brown = (143, 71, 0)

pygame.init()

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Singing Bird!")

done = False

clock = pygame.time.Clock() #for frame per sec(fps)


def obstacle(xloc, xsize, yloc, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, yloc + ysize + space, xsize, ysize + 500])
    pygame.draw.rect(screen, black, [xloc + 63, yloc, 7, ysize])
    pygame.draw.rect(screen, grey, [xloc + 56, yloc, 7, ysize])
    pygame.draw.rect(screen, grey2, [xloc + 49, yloc, 7, ysize])
    pygame.draw.rect(screen, green2, [xloc, yloc, 7, ysize])
    pygame.draw.rect(screen, green3, [xloc + 7, yloc, 7, ysize])

    pygame.draw.rect(screen, black, [xloc + 63, yloc + ysize + space, 7, ysize + 500])
    pygame.draw.rect(screen, grey, [xloc + 56, yloc + ysize + space, 7, ysize + 500])
    pygame.draw.rect(screen, grey2, [xloc + 49, yloc + ysize + space, 7, ysize + 500])
    pygame.draw.rect(screen, green2, [xloc, yloc + ysize + space, 7, ysize + 500])
    pygame.draw.rect(screen, green3, [xloc + 7, yloc + ysize + space, 7, ysize + 500])


def bird(x, y):
    pygame.draw.circle(screen, yellow, [x, int(y)], 20)
    pygame.draw.circle(screen, white, [int(x + 12), int(y - 12)], 10)
    pygame.draw.polygon(screen, orange, [(x + 12, y + 5), (x + 12, y - 5), (x + 25, y)])
    pygame.draw.circle(screen, black, [int(x + 12), int(y - 12)], 1)
    pygame.draw.circle(screen, black, [int(x - 12), int(y + 10)], 11)
    pygame.draw.circle(screen, yellow, [int(x - 12), int(y + 10)], 10)


def gameover():
    font = pygame.font.Font(None, 50)
    text = font.render("Game over", True, black)
    screen.blit(text, [150, 250])


def Score(score):
    font = pygame.font.Font(None, 50)
    text = font.render(("Score: " + str(score)), True, black)
    screen.blit(text, [0, 0])


def cloud(clx, cly):
    pygame.draw.circle(screen, grey3, [int(clx), int(cly)], 20)
    pygame.draw.circle(screen, grey3, [int(clx + 15), int(cly - 10)], 20)
    pygame.draw.circle(screen, grey3, [int(clx + 30), int(cly)], 20)
    pygame.draw.circle(screen, grey3, [int(clx + 15), int(cly + 10)], 20)


def Ground(ground):
    pygame.draw.rect(screen, brown, [0, ground, 700, 60])



# Initilization

xloc = 700
xsize = 70
yloc = 0
ysize = randint(0, 325)
x = 350
y = 250
yspeed = 0
ground = 494.5
obspeed = 1
space = 150
limit = -80
score = 0

while not done:
    data = stream.read(CHUNK)  #Fragment initialization
    reading = audioop.max(data, 2)
    print(reading)

    time.sleep(0.00000000000001)
    if reading>10000:
        yspeed=-1.75
    if reading<10000:
       yspeed=1.5
    for event in pygame.event.get():
        pass
    if event.type == pygame.QUIT:
        done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            yspeed = -1.75
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            yspeed = 1.5

  #Background

    screen.fill(blue)

    cloud(45, 40)
    cloud(83, 482)
    cloud(383, 39)
    cloud(524, 23)
    cloud(467, 63)
    cloud(623, 424)
    cloud(330, 260)
    cloud(600, 150)
    cloud(150, 150)
    cloud(450, 400)
    obstacle(xloc, xsize, yloc, ysize)
    bird(x, y)
    Score(score)

    if y + 20 > ground:
        gameover()
        obspeed = 0
        yspeed = 0

    else:
        xloc -= obspeed
        y += yspeed

    if x + 20 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:
        gameover()
        obspeed = 0
        yspeed = 0

    else:
        xloc -= obspeed
        y += yspeed

    if x + 20 > xloc and y + 20 > ysize + space and x - 15 < xsize + xloc:
        gameover()
        obspeed = 0
        yspeed = 0

    else:
        xloc -= obspeed
        y += yspeed

    if xloc < limit:
        ysize = randint(0, 400)
        xloc = 700

    else:
        xloc -= obspeed
        y += yspeed

    if x > xloc and x < xloc + 3:
        score = (score + 1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
