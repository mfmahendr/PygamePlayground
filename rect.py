import pygame

pygame.init()
screenSize = [1920, 720]
screen = pygame.display.set_mode(screenSize)
color = pygame.Color(0, 0, 255)
clock = pygame.time.Clock()

rect_size = 100

done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this lo

    screen.fill("white")

    posX = 0
    posY = 0
    for i in range (3):
        pygame.draw.rect(screen, color, [posX, posY, rect_size, rect_size], 10)
        posX += rect_size
        posY += rect_size
    pygame.display.flip()