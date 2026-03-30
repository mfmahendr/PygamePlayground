import pygame
import argparse

parser = argparse.ArgumentParser()

# input
rect_size = 100
n = 3
line_width = 10

parser.add_argument("size", help="rectangular size or circle diameter to draw")
parser.add_argument("width", help="line width for the shapes to draw")
parser.add_argument("n", help="number of shapes to draw")
args = parser.parse_args()
if args.n:
    n = int(args.n)
if args.size:
    rect_size = int(args.size)
if args.width:
    line_width = int(args.width)

pygame.init()
total_rect_width = (rect_size+line_width)*n
if (total_rect_width > 1080):
    total_rect_width = 1080
if (total_rect_width < 500):
    total_rect_wisth = 500

screenSize = [total_rect_width, total_rect_width]
screen = pygame.display.set_mode(screenSize)
color = pygame.Color(0, 0, 255)
clock = pygame.time.Clock()

done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this lo

    screen.fill("white")

    posX = 0
    posY = 0
    radius = rect_size/2
    for i in range (n):
        pygame.draw.rect(screen, color, [posX, posY, rect_size, rect_size], line_width)
        pygame.draw.circle(screen, color, [posX+radius, radius], radius, line_width)
        posX += rect_size
    pygame.display.flip()