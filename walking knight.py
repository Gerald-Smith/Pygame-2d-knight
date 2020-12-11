import pygame
import time
pygame.init()
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("TITLE PLACE HOLDER")

walkRight = pygame.image.load('sprites/knight_walk_right.png')
walkLeft = pygame.image.load('sprites/knight_walk_left.png')
walkDown = pygame.image.load('sprites/knight_walk_down.png')
walkUp = pygame.image.load('sprites/knight_walk_up.png')
background = pygame.image.load('sprites/background.png')
charX = 64
charY = 64
charWidth = 120
charHeight = 120
charVelocity = 7
left = False
right = False
down = False
up = False
prevImage = pygame.image.load('sprites/knight_walk_down.png')

clock = pygame.time.Clock()

def redrawGameWindow():
    global prevImage
    window.blit(background, (0, 0))
    if left:
        window.blit(walkLeft, (charX, charY))
        prevImage = pygame.image.load('sprites/knight_walk_left.png')
    elif right:
        window.blit(walkRight, (charX, charY))
        prevImage = pygame.image.load('sprites/knight_walk_right.png')
    elif down:
        window.blit(walkDown, (charX, charY))
        prevImage == pygame.image.load('sprites/knight_walk_down.png')
    elif up:
        window.blit(walkUp, (charX, charY))
        prevImage == pygame.image.load('sprites/knight_walk_up.png')
    else:
        window.blit(prevImage, [charX, charY])
    pygame.display.update()

run = True
while run:
    clock.tick(27)
    redrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and charX > charVelocity - 35:
        charX -= charVelocity
        left = True
        right = False
        down = False
        up = False
        time.sleep(0.01)
    elif keys[pygame.K_d] and charX < 1050 - charWidth - charVelocity:
        charX += charVelocity
        right = True
        left = False
        down = False
        up = False
        time.sleep(0.01)
        walkCount = 0
    elif keys[pygame.K_w] and charY > charVelocity:
        charY -= charVelocity
        up = True
        down = False
        right = False
        left = False
        time.sleep(0.01)
    elif keys[pygame.K_s] and charY < 650 - charHeight - charVelocity:
        charY += charVelocity
        down = True
        up = False
        right = False
        left = False
        time.sleep(0.01)
    else:
        right = False
        left = False
        down = False
        up = False
        time.sleep(0.01)
pygame.quit()
