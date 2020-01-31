import pygame
from random import randint
import time, audioop
import pyaudio
SAMPLErate = 48000
TIMEdivlx = [0.2, 0.5, 1.0,2.0,5.0,10.0]
TIMEdiv = 0

CHUNK = int( float(SAMPLErate) * TIMEdivlx[TIMEdiv])
FORMAT = pyaudio.paInt16
CHANNELS =  1
RATE = 88200

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, rate=RATE,input=True, frames_per_buffer = CHUNK, channels = CHANNELS)



pygame.init()
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
size=700,500
x_speed = 0
y_speed = 0
ground = 480
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,350)
space = 100
obspeed = 2.5
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Singing Bird")

done = False
clock = pygame.time.Clock()
def obstacles(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, int(yloc+space+xsize), xsize, 500])




def ball(x,y):
    pygame.draw.circle(screen, black, [x,y],20)

x=350
y=250

while not done:

    #for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #        done = True
    #    if event.type == pygame.KEYDOWN:
    #        if event.key == pygame.K_UP:
    #            y_speed = -7
    #    if event.type == pygame.KEYUP:
    #        if event.key == pygame.K_UP:
    #            y_speed = 4
    data = stream.read(CHUNK)
    reading = audioop.max(data, 2)
    #print(reading)

    time.sleep(.000000000000000000000000001)

    if reading>10000:
        y_speed=-7
    if reading<10000:
        y_speed=4



    screen.fill(white)
    ball(x,y)
    obstacles(xloc, yloc, xsize, ysize)
    pygame.display.flip()
    y+=y_speed
    xloc+=obspeed
    #if y>ground:
     #   gameover()
      #  y_speed=0
    clock.tick(200)
pygame.quit()