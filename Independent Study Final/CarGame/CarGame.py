import pygame
import time
import random


pygame.init()

display_width = 1000
display_height = 760

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Don\'t Crash')
clock = pygame.time.Clock()

carimg = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/carpic.png')
carleftimg = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/carpicleft.png')
carrightimg = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/carpicright.png')
sidewalkimg = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/sidewalk.png')
bluecar = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/bluecar.png')
orangecar = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/orangecar.png')
redcar = pygame.image.load('C:/Users/techa/PycharmProjects/CarGame/redcar.png')

def car(x,y):
    gameDisplay.blit(carimg, (x, y))

def carleft(x,y):
    gameDisplay.blit(carleftimg, (x, y))

def carright(x,y):
    gameDisplay.blit(carrightimg, (x,y))

def blucar(x,y):
    gameDisplay.blit(bluecar,(x,y))

def orngcar(x,y):
    gameDisplay.blit(orangecar, (x,y))

def rcar(x,y):
    gameDisplay.blit(redcar, (x,y))

def sidewalk(x,y):
    gameDisplay.blit(sidewalkimg, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 118)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)


def crash():
    message_display('You Crashed')
    gameloop()





def gameloop(): #The Game itself

    over = False

    x = (display_width/2)
    y = (display_height*.8)

    x_change = 0

    top_speed = 5

    car_startx = random.randrange(200, display_width - 240)
    car_starty = -300
    car_speed = random.randrange(1,top_speed)
    through = 0
    car2_startx = random.randrange(200, display_width - 240)
    car2_starty = -300
    car2_speed = random.randrange(1, top_speed)
    rcar_startx = random.randrange(200, display_width - 240)
    rcar_starty = -300
    rcar_speed = random.randrange(1, top_speed)

    #this will make sure cars dont spawn in the same lane and overlap
    if car2_startx > (car_startx-50) and car2_startx < car_startx+100 and car2_speed > car_speed:
        if car_startx < display_width/2:
            car2_startx = random.randrange(car_startx + 50, display_width-240)
        elif car_startx > display_width/2:
            car2_startx = random.randrange(200, car_startx)
    if (car2_startx+100) > car_startx and (car2_startx-50) < car_startx and car2_speed < car_speed:
        if car2_startx < display_width/2:
            car_startx = random.randrange(car2_startx + 50, display_width-240)
        elif car2_startx > display_width/2:
            car_startx = random.randrange(200, car2_startx)
    if rcar_startx > (car_startx - 50) and rcar_startx < car_startx + 100 and rcar_speed > car_speed:
        if car_startx < display_width / 2:
            rcar_startx = random.randrange(car_startx + 50, display_width - 240)
        elif car_startx > display_width / 2:
            rcar_startx = random.randrange(200, car_startx)
    if rcar_startx > (car_startx - 50) and rcar_startx < car_startx + 100 and rcar_speed < car_speed:
        if rcar_startx < display_width / 2:
            car_startx = random.randrange(rcar_startx + 50, display_width - 240)
        elif rcar_startx > display_width / 2:
            car_startx = random.randrange(200, rcar_startx)

    if rcar_startx > (car2_startx - 50) and rcar_startx < car2_startx + 100 and rcar_speed > car2_speed:
        if car2_startx < display_width / 2:
            rcar_startx = random.randrange(car2_startx + 50, display_width - 240)
        elif car2_startx > display_width / 2:
            rcar_startx = random.randrange(200, car2_startx)
    if rcar_startx > (car2_startx - 50) and rcar_startx < car2_startx + 100 and rcar_speed < car2_speed:
        if rcar_startx < display_width / 2:
            car2_startx = random.randrange(rcar_startx + 50, display_width - 240)
        elif rcar_startx > display_width / 2:
            car2_startx = random.randrange(200, rcar_startx)


    while not over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0



        x += x_change

        gameDisplay.fill(black)

        blucar(car_startx,car_starty)
        car_starty += car_speed

        if top_speed >= 10:
            top_speed = 10


        if car_starty > display_height+350:
            car_starty = -300
            car_startx = random.randrange(200, display_width-240)
            car_speed = random.randrange(1,top_speed)
            through += 1
            top_speed += 1
            if (car2_startx + 100) > car_startx and (car2_startx - 50) < car_startx and car2_speed < car_speed:
                if car2_startx < display_width / 2:
                    car_startx = random.randrange(car2_startx + 50, display_width - 240)
                elif car2_startx > display_width / 2:
                    car_startx = random.randrange(200, car_startx)
            if rcar_startx > (car_startx - 50) and rcar_startx < car_startx + 100 and rcar_speed < car_speed:
                if rcar_startx < display_width / 2:
                    car_startx = random.randrange(rcar_startx + 50, display_width - 240)
                elif rcar_startx > display_width / 2:
                    car_startx = random.randrange(200, rcar_startx)
        if through >= 1:
            orngcar(car2_startx, car2_starty)
            car2_starty += car2_speed
            if car2_starty > display_height+350:
                car2_startx = random.randrange(200, display_width - 240)
                car2_starty = -300
                car2_speed = random.randrange(1, top_speed)
                if car2_startx > (car_startx - 50) and car2_startx < car_startx + 100 and car2_speed > car_speed:
                    if car_startx < display_width / 2:
                        car2_startx = random.randrange(car_startx + 50, display_width - 240)
                    elif car_startx > display_width / 2:
                        car2_startx = random.randrange(200, car_startx)
                if rcar_startx > (car2_startx - 50) and rcar_startx < car2_startx + 100 and rcar_speed < car2_speed:
                    if rcar_startx < display_width / 2:
                        car2_startx = random.randrange(rcar_startx + 50, display_width - 240)
                    elif rcar_startx > display_width / 2:
                        car2_startx = random.randrange(200, rcar_startx)
        if through >=3:
            rcar(rcar_startx, rcar_starty)
            rcar_starty += rcar_speed
            if rcar_starty > display_height+350:
                rcar_startx = random.randrange(200, display_width - 240)
                rcar_starty = -300
                rcar_speed = random.randrange(1, top_speed)
                if rcar_startx > (car_startx - 50) and rcar_startx < car_startx + 100 and rcar_speed > car_speed:
                    if car_startx < display_width / 2:
                        rcar_startx = random.randrange(car_startx + 50, display_width - 240)
                    elif car_startx > display_width / 2:
                        rcar_startx = random.randrange(200, car_startx)
                if rcar_startx > (car2_startx - 50) and rcar_startx < car2_startx + 100 and rcar_speed > car2_speed:
                    if car2_startx < display_width / 2:
                        rcar_startx = random.randrange(car2_startx + 50, display_width - 240)
                    elif car2_startx > display_width / 2:
                        rcar_startx = random.randrange(200, car2_startx)

        if x_change == 0:
            car(x,y)
        elif x_change < 0:
            carleft(x,y)
        elif x_change > 0:
            carright(x,y)


        if y <= car_starty+90 and y >= car_starty-90:
            if x >= (car_startx-50) and x <= (car_startx+50):
                crash()

        if y <= car2_starty+90 and y >= car2_starty-90:
            if x >= (car2_startx-50) and x <= (car2_startx+50):
                crash()

        if y <= rcar_starty+90 and y >= rcar_starty-90:
            if x >= (rcar_startx-50) and x <= (rcar_startx+50):
                crash()


        if x <= 176:
            crash()
        elif x >= (display_width - (176+64)):
            crash()


        sidewalk(0,0)
        sidewalk(0,424)
        sidewalk((display_width-176), 0)
        sidewalk((display_width-176), 424)
        pygame.display.update()

    while over:
        pygame.quit()
        quit()

gameloop()

pygame.quit()
quit()