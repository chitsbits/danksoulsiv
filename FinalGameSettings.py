#########################################
# Filename: FinalGameSettings_1
# Description: Final Game settings version 1
# Author: Sunny Jiao
# Date: 12/22/18
#########################################

import pygame
pygame.mixer.pre_init(44100, -16, 1, 2048)
pygame.init()

WIDTH = 1000
HEIGHT = 600
SPRITE_X_OFFSET = 160
SPRITE_Y_OFFSET = 40
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Version 2")
FPS = 60

GROUND = HEIGHT - 50

outline = 0

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
BLUE = (  0,  0,255)
YELLOW = (255,255,  0)
RED = (255,  0,  0)

# Game Properties
gameOver = False
debugMode = False

# Player Properties
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 160
PLAYER_X_SPEED = 4
PLAYER_Y_SPEED = 0.5
PLAYER_X_HIT_SPEED = 0.2
PLAYER_DASH_SPEED = 8
JUMP_SPEED = -25

hitboxOffset = 200

# Physics
GRAVITY = 1.5

# Background image import
lake = pygame.image.load("img/backgrounds/lake.png").convert()
volcano = pygame.image.load("img/backgrounds/volcano.png").convert()
space = pygame.image.load("img/backgrounds/space.png").convert()
planet = pygame.image.load("img/backgrounds/planet.png").convert()

waterfall = [0] * 8
for i in range(8):
    waterfall[i] = pygame.image.load("img/backgrounds/waterfall/waterfall" + str(i) + ".png").convert()
menupic = [0] * 22
for i in range(22):
    menupic[i] = pygame.image.load("img/backgrounds/menu/menupic" + str(i) + ".png").convert()

# Other images
controls = pygame.image.load("img/controls.png").convert()

# Audio
pygame.mixer.music.load("sounds/menumusic.ogg")
pygame.mixer.music.set_volume(0.2)

audioDeath = pygame.mixer.Sound("sounds/dead.wav")
audioGameStart = pygame.mixer.Sound("sounds/gamestart.wav")
audioMenuMove = pygame.mixer.Sound("sounds/menumove.wav")
audioLightSwing = pygame.mixer.Sound("sounds/lightswing.wav")
audioHeavySwing = pygame.mixer.Sound("sounds/heavyswing.wav")
audioHurt = pygame.mixer.Sound("sounds/ouch.wav")
audioStep = pygame.mixer.Sound("sounds/step.wav")
audioShield = pygame.mixer.Sound("sounds/shield.wav")
audioDash = pygame.mixer.Sound("sounds/dash.wav")
audioLargePullout = pygame.mixer.Sound("sounds/largepullout.wav")
audioLargeHit = pygame.mixer.Sound("sounds/largehit.wav")
audioKick = pygame.mixer.Sound("sounds/kick.wav")
audioOk = pygame.mixer.Sound("sounds/ok.wav")
audioCancel = pygame.mixer.Sound("sounds/cancel.wav")
audioJump = pygame.mixer.Sound("sounds/jump.wav")
audioDive = pygame.mixer.Sound("sounds/dive.wav")

audioDeath.set_volume(0.2)
audioGameStart.set_volume(0.2)
audioMenuMove.set_volume(0.2)
audioLightSwing.set_volume(0.1)
audioHeavySwing.set_volume(0.1)
audioShield.set_volume(0.1)
audioHurt.set_volume(0.2)
audioStep.set_volume(0.1)
audioDash.set_volume(0.6)
audioLargePullout.set_volume(0.2)
audioLargeHit.set_volume(0.2)
audioKick.set_volume(0.2)
audioCancel.set_volume(0.2)
audioOk.set_volume(0.2)
audioJump.set_volume(0.1)
audioDive.set_volume(0.1)
