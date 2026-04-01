import pygame
import argparse
import math

parser = argparse.ArgumentParser()

# input
circle_diameter = 100
n = 3
line_width = 10

## CLI argument
parser.add_argument("length", help="initial rectangular length")
parser.add_argument("height", help="initial rectangular height")
parser.add_argument("linewidth", help="line width for the shape to draw")
parser.add_argument("n", help="number of shape rotating")
args = parser.parse_args()
if args.length:
    length = int(args.length)
if args.height:
    height = int(args.height)
if args.linewidth:
    line_width = int(args.linewidth)
if args.n:
    n = int(args.n)

## pygame configurations
pygame.init()
screen_size = 720
screen = [screen_size, screen_size]
screen = pygame.display.set_mode(screen)
color = pygame.Color(0, 0, 255)
clock = pygame.time.Clock()

pivot = screen_size/2

## coordinete initialization
Rtl = pygame.math.Vector2(-(length/2), -(height/2))
Rtr = pygame.math.Vector2(+(length/2), -(height/2))
Rbl = pygame.math.Vector2(-(length/2), +(height/2))
Rbr = pygame.math.Vector2(+(length/2), +(height/2))

pivotR = pygame.math.Vector2(pivot, pivot)

done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this lo

    screen.fill("white")

    vtl = pivotR - Rtl
    vtr = pivotR - Rtr
    vbl = pivotR - Rbl
    vbr = pivotR - Rbr

    # operation start here
    radius = circle_diameter/2
    for i in range (n):
        pygame.draw.polygon(screen, color, [vtl, vtr, vbr, vbl], line_width)
        vtl = (vtl-pivotR).rotate(15)+pivotR
        vbl = (vbl-pivotR).rotate(15)+pivotR
        vtr = (vtr-pivotR).rotate(15)+pivotR
        vbr = (vbr-pivotR).rotate(15)+pivotR
    pygame.display.update()
        
