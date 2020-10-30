import pygame
import random
import math

# initialize pygame
pygame.init()

# creating screen

screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('Back.png')
pygame.display.set_caption("kya_kiye_Koot_diye")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player

playerImg = pygame.image.load('player.png')
playerX = 350.0
playerY = 500
playerX_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change =[]
enemyY_change =  []
num=6
for i in range(num):

    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change .append(2)
    enemyY_change.append(30)

webImg = pygame.image.load('web.png')
webX = 0
webY = 500
webX_change = 0
webY_change = 5
web_state = "ready"  # ready is not in motion

#score
score=0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


def fire_web(x, y):
    global web_state
    web_state = "fire"
    screen.blit(webImg, (x + 16, y + 10))


def isCollision(webX, webY, enemyX, enemyY):
    dist = math.sqrt((math.pow(enemyX - webX, 2)) + (math.pow(enemyY - webY, 2)))
    if dist < 27:
        return True
    else:
        return False

    # dist = math.sqrt(math.pow((webX-enemyX),2)+math.pow((webY-enemyY),2))
    # if dist <27:


# Game loop
running = True

while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    # playerX = playerX + 0.4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_SPACE:
                if web_state is "ready":
                    webX = playerX
                    fire_web(playerX, webY)
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740
    for i in range(num):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(webX, webY, enemyX[i], enemyY[i])
        if collision:
            webY = 500
            web_state = "ready"
            score += 1
            print(score)
            enemyX[i]= random.randint(0, 700)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)

    if webY <= 0:
        webY = 500
        web_state = "ready"
    if web_state is "fire":
        #  webX=playerX
        fire_web(webX, webY)
        webY -= webY_change




    player(playerX, playerY)

    pygame.display.update()
