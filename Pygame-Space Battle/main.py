import pygame
import random
import math
from pygame import mixer

# initializing the pygame
pygame.init()

# creating a screen
screen = pygame.display.set_mode((800, 600))

# background music
mixer.music.load("bg1.mp3")
mixer.music.play(-1)

# title and icons
pygame.display.set_caption("Manish's Game")
icon = pygame.image.load('i_ufo.png')
pygame.display.set_icon(icon)

# Player Position
playerImg = pygame.image.load('i_shuttle.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy Position
enImg =[]
enX = []
enY = []
enX_change = []
enY_change = []
en_number = 6
for i in range(en_number):
    enImg.append(pygame.image.load('ufo2.png'))
    enX.append(random.randint(0, 670))
    enY.append(random.randint(0, 100))
    enX_change.append(0.3)
    enY_change.append(0.1)

def enemy(x,y,i):
    screen.blit(enImg[i], (x, y))

# Background Position
bgImg = pygame.image.load('sp2.png')
bgX = 0
bgY = 0
def background():
    screen.blit(bgImg, (bgX, bgY))

# Bullet Position
bulletImg = pygame.image.load('bullet.png')
bulletX = 400
bulletY = 480
bulletX_change = 0
bulletY_change =2
bullet_state = "ready"
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+50, y-60))

# collision
def collision(enX,enY, bulletX,bulletY):
    distance = math.sqrt(math.pow(enX - bulletX, 2)+math.pow(enY - bulletY, 2))
    if distance <= 70:
        return True
    else:
        return False
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def score(x,y):
    score = font.render("Score: "+ str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))
# game over text
_value = 0
over_font = pygame.font.Font('freesansbold.ttf',32)
overX = 100
overY = 100
def game_over(x,y):
    over = font.render("GAME OVER: "+ str(score_value), True, (0,0,0))
    screen.blit(over, (x,y))





# game loop
running = True
while running:
    # to change the screen color
    #screen.fill((0, 255, 255))
    background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_sound = mixer.Sound("bg5.wav")
                    bullet_sound.play()
                    bullet(bulletX, bulletY)
            if event.key == pygame.K_DOWN:
                pause = True
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                # print("left")
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_1 or event.key == pygame.K_2:
                playerX_change = 0
                playerY_change = 0

    # player change condition
    playerX += playerX_change
    if playerX <= -28:
        playerX = -28
    elif playerX >= 700:
        playerX = 700
    # enemy change condition
    #bullet state
    for i in range(en_number):
        # game over
        if enY[i]>=400:
            for j in range(en_number):
                enY[j] = 2000
            game_over(overX,overY)
            break

        enX[i] += enX_change[i]
        enY[i] += enY_change[i]
        if enX[i] >= 670:
            enX_change[i] = -0.3
        elif enX[i] <= 0:
            enX_change[i] = 0.3
        # if collided
        collided = collision(enX[i], enY[i], bulletX, bulletY)
        if collided:
            collision_sound = mixer.Sound("bg4.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score)
            enX[i] = random.randint(0, 670)
            enY[i] = random.randint(0, 150)
        enemy(enX[i], enY[i], i)

    if bulletY<=0:
        bullet_state="ready"
        bulletY = playerY+70
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    score(textX, textY)
    pygame.display.update()
