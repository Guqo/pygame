import pygame
from pygame.locals import *
import random
import pymsgbox

size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1
y = 0
cars = 0
pygame.font.init()
my_font = pygame.font.SysFont('Roboto', 30)

pygame.init()
running = True
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Car Dodger")
screen.fill((60, 200, 0))

pygame.display.update()

# player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.75

# enemy vehicle
car2 = pygame.image.load("carEnemy.png")
car2_loc = car.get_rect()
car2_loc.center = left_lane, height * 0

counter = 0

while running:
    # levely
    counter += 1
    if counter == 5000:
        speed += 0.25
        counter = 0
    # animace
    y += speed
    car2_loc[1] = y
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
        y = -200
        cars += 1
    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 300 and car2_loc[1] < car_loc[1] + 300:
        break
    # eventy
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT] and car_loc[0] > 206:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT] and car_loc[0] < 456:
                car_loc = car_loc.move([int(road_w/2), 0])
    # cesta
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))
    # vykreslení
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    text_surface = my_font.render('Score: ' + str(cars), False, (0, 0, 0), (60, 200, 0))
    screen.blit(text_surface, (0,0))
    pygame.display.update()

pymsgbox.alert('Game Over!', 'Car Dodger')
pygame.quit()
