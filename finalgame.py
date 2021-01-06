#########################################
# Filename: finalgame.py
# Description: Final Game version 2
# Author: Sunny Jiao
# Date: 01/12/19
#########################################

import time
import pygame

# All game constants (e.g. width, height, colours, gravity, playersize, etc. are located in this class)
from FinalGameSettings import *
from FinalGameClasses import *

pygame.init()

font1 = pygame.font.SysFont("Arial",15)
font2 = pygame.font.SysFont("Uroob",25)
font3 = pygame.font.SysFont("Uroob",45)
font4 = pygame.font.SysFont("Uroob",50)

headerRed = font2.render("Red Solaire",1,WHITE)
headerWhite = font2.render("White Solaire",1,WHITE)
headerWinnerR = font3.render("RED WINS",1,WHITE)
headerWinnerW = font3.render("WHITE WINS",1,WHITE)

title = font1.render("wanna sprite cranberry",1,WHITE)

pygame.mixer.music.play(-1)

#---------------------------------------#
# Functions                             #
#---------------------------------------#

def muteSfx():
    audioDeath.set_volume(0)
    audioGameStart.set_volume(0)
    audioMenuMove.set_volume(0)
    audioLightSwing.set_volume(0)
    audioHeavySwing.set_volume(0)
    audioShield.set_volume(0)
    audioHurt.set_volume(0)
    audioStep.set_volume(0)
    audioDash.set_volume(0)
    audioLargePullout.set_volume(0)
    audioLargeHit.set_volume(0)
    audioKick.set_volume(0)
    audioCancel.set_volume(0)
    audioOk.set_volume(0)
    audioJump.set_volume(0)
    audioDive.set_volume(0)

def unMuteSfx():
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

def drawMainMenu():
    gameWindow.fill(BLACK)
    gameWindow.blit(menupic[int(menupicTimer.count)],(0,0))
    gameWindow.blit(title,(WIDTH/2 - title.get_width()/2, HEIGHT/4 + title.get_height()/2))
    
    titlePlayColour = WHITE
    titleOptionsColour = WHITE
    titleControlsColour = WHITE
    titleQuitColour = WHITE
    if menuSelect == 0:
        titlePlayColour = YELLOW
    elif menuSelect == 1:
        titleOptionsColour = YELLOW
    elif menuSelect == 2:
        titleControlsColour = YELLOW
    elif menuSelect == 3:
        titleQuitColour = YELLOW
        
    titlePlay = font4.render("play",1,titlePlayColour)
    titleOptions = font4.render("options",1,titleOptionsColour)
    titleControls = font4.render("controls",1,titleControlsColour)
    titleQuit = font4.render("quit",1,titleQuitColour)

    gameWindow.blit(titlePlay, (WIDTH/2 - titlePlay.get_width()/2, HEIGHT/2 - 75))
    gameWindow.blit(titleOptions, (WIDTH/2 - titleOptions.get_width()/2, HEIGHT/2))
    gameWindow.blit(titleControls,(WIDTH/2 - titleControls.get_width()/2, HEIGHT/2 + 75))
    gameWindow.blit(titleQuit, (WIDTH/2 - titleQuit.get_width()/2, HEIGHT/2 + 150))

    if inControls:
        gameWindow.blit(controls, (0,0))

    pygame.display.update()

def drawOptions():
    gameWindow.fill(BLACK)
    optionsFullscreenColour = WHITE
    optionsTimerColour = WHITE
    optionsMusicColour = WHITE
    optionsSfxColour = WHITE
    
    if optionsSelect == 0:
        optionsFullscreenColour = YELLOW
    elif optionsSelect == 1:
        optionsTimerColour = YELLOW
    elif optionsSelect == 2:
        optionsMusicColour = YELLOW
    elif optionsSelect == 3:
        optionsSfxColour = YELLOW

    if pygame.Surface.get_flags(gameWindow) == 0x80000000:  # -> Fullscreen flag
        fullscreenOnOff = "ON"
    else:
        fullscreenOnOff = "OFF"

    if timerEnabled:
        timerOnOff = "ON"
    else:
        timerOnOff = "OFF"

    if musicEnabled:
        musicOnOff = "ON"
    else:
        musicOnOff = "OFF"

    if sfxEnabled:
        sfxOnOff = "ON"
    else:
        sfxOnOff = "OFF"

    optionsFullscreen = font4.render("fullscreen: " + fullscreenOnOff,1,optionsFullscreenColour)
    optionsTimer = font4.render("timer: " + timerOnOff,1,optionsTimerColour)
    optionsMusic = font4.render("music: " + musicOnOff,1,optionsMusicColour)
    optionsSfx = font4.render("sfx: " + sfxOnOff,1,optionsSfxColour)

    gameWindow.blit(optionsFullscreen, (WIDTH/2 - optionsFullscreen.get_width()/2, HEIGHT/2 - 75))
    gameWindow.blit(optionsTimer, (WIDTH/2 - optionsTimer.get_width()/2, HEIGHT/2))
    gameWindow.blit(optionsMusic,(WIDTH/2 - optionsMusic.get_width()/2, HEIGHT/2 + 75))
    gameWindow.blit(optionsSfx, (WIDTH/2 - optionsSfx.get_width()/2, HEIGHT/2 + 150))

    pygame.display.update()

def drawGameWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(lake, (0,0))

    # Timer
    if timerEnabled:
        timer = font4.render(str(timeLeft),1,WHITE)
        gameWindow.blit(timer,(WIDTH/2 - timer.get_width()/2, 65))
    
    # Health bars
    gameWindow.blit(headerRed, (50, 45))
    pygame.draw.rect(gameWindow, WHITE, (49, 74, 402, 17), 1)
    if p2.hp > 0:
        pygame.draw.rect(gameWindow, YELLOW, (50, 75, int(p2.hpPast * 4),15), outline)
        pygame.draw.rect(gameWindow, RED, (50, 75, int(p2.hp * 4), 15), outline)

    gameWindow.blit(headerWhite, (850, 45))
    pygame.draw.rect(gameWindow, WHITE, (549, 74, 402, 17), 1)
    if p1.hp > 0:
        pygame.draw.rect(gameWindow, YELLOW, (550, 75, int(p1.hpPast * 4),15), outline)
        pygame.draw.rect(gameWindow, RED, (550, 75, int(p1.hp * 4), 15), outline)

    # Draw players
    p1.drawSprite()
    p2.drawSprite()

    # Draw winner screen
    if gameOver:
        pygame.draw.rect(gameWindow, BLACK, (WIDTH/2 - 100, 190, 200, 50), outline)
        if p1.hp < p2.hp:
            gameWindow.blit(headerWinnerR, (WIDTH/2 - headerWinnerR.get_width()/2, 200))
        else:
            gameWindow.blit(headerWinnerW, (WIDTH/2 - headerWinnerW.get_width()/2, 200))
    
    # Debug info
    if debugMode:
        drawDebugScreen()
    pygame.display.update()


def drawDebugScreen():
    debugPos = font1.render("POS:   x: "+str(round(p1.posX,2))+"  y: "+str(round(p1.posY,2)),1,WHITE)
    frameNo = font1.render(str(frame),1,WHITE)
    debugInputFrame = font1.render("comboDelay: "+str(p1.comboDelay.count),1,WHITE)
    debugAtkDelay = font1.render("atkDelay: "+str(p1.attackDelay.count),1,WHITE)
    debugPlayerState = font1.render("playerstate: "+str(p1.playerState),1,WHITE)
    dbP2hp = font1.render(str(p2.hp),1,WHITE)
    dbP1hp = font1.render(str(p1.hp),1,WHITE)
    dbDashTimer = font1.render("dash: "+str(p1.moveInputTimer.count),1,WHITE)
    dbCanAttack = font1.render("canAttack: "+str(p1.canAttack),1,WHITE)
    dbWindup = font1.render("windup: "+str(p1.attackWindup.count),1,WHITE)

    pygame.draw.rect(gameWindow, RED, p1.attackHitbox, 2)
    pygame.draw.rect(gameWindow, RED, p2.attackHitbox, 2)
    pygame.draw.rect(gameWindow, YELLOW, p1.blockHitbox, 2)
    pygame.draw.rect(gameWindow, YELLOW, p2.blockHitbox, 2)

    pygame.draw.rect(gameWindow, BLUE, p1.bodyHitbox, 2)
    pygame.draw.rect(gameWindow, BLUE, p2.bodyHitbox, 2)
    pygame.draw.circle(gameWindow, RED, (int(p1.posX), int(p1.posY)), 2, outline)
    pygame.draw.circle(gameWindow, RED, (int(p2.posX), int(p2.posY)), 2, outline)
    
    gameWindow.blit(frameNo, (0, 100))
    gameWindow.blit(debugPos,(0,120))
    gameWindow.blit(debugInputFrame, (0,140))
    gameWindow.blit(debugAtkDelay, (0,160))
    gameWindow.blit(debugPlayerState,(0,180))
    gameWindow.blit(dbP2hp,(200,50))
    gameWindow.blit(dbP1hp,(700,50))
    gameWindow.blit(dbDashTimer,(0,200))
    gameWindow.blit(dbCanAttack,(0,220))
    gameWindow.blit(dbWindup,(0,240))

#---------------------------------------#
# Main program                          #
#---------------------------------------#
clock = pygame.time.Clock()

fullscreenEnabled = False
timerEnabled = True
musicEnabled = True
sfxEnabled = True

inGame = True
quitGame = False
inControls = False
inMenu = True

while inGame:
    menuSelect = 0
    menupicTimer = FrameTimer(22)

#---------------------------------------#
# Menu Loop                             #
#---------------------------------------#
    # Main Menu
    while inMenu:
        drawMainMenu()
        clock.tick(FPS)
        # Background animation
        menupicTimer.increment(0.2)
        if menupicTimer.timeUp():
            menupicTimer.reset()
        
        # Main menu inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame = True
                inMenu = False
            elif event.type == pygame.KEYDOWN:
                # Menu navigation
                if event.key == pygame.K_DOWN:
                    menuSelect = (menuSelect + 1) % 4
                    audioMenuMove.play()
                if event.key == pygame.K_UP:
                    menuSelect = (menuSelect - 1) % 4
                    audioMenuMove.play()
                # Selection input
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    inControls = False
                    audioOk.play()

                    # Play
                    if menuSelect == 0:
                        inMenu = False
                        audioGameStart.play()

                    # Options Menu button
                    # fullscreen, timer, music, sfx
                    elif menuSelect == 1:
                        inOptions = True
                        optionsSelect = 0
                        
                        while inOptions:
                            drawOptions()
                            clock.tick(FPS)
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    quitGame = True
                                    inControls = False
                                    
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        inOptions = False
                                        audioCancel.play()
                                    elif event.key == pygame.K_DOWN:
                                        optionsSelect = (optionsSelect + 1) % 4
                                        audioMenuMove.play()
                                    elif event.key == pygame.K_UP:
                                        optionsSelect = (optionsSelect - 1) % 4
                                        audioMenuMove.play()
                                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                                        audioOk.play()
                                        # Fullscreen
                                        if optionsSelect == 0:
                                            pygame.display.toggle_fullscreen()
                                        # Timer
                                        elif optionsSelect == 1:
                                            if timerEnabled:
                                                timerEnabled = False
                                            else:
                                                timerEnabled = True
                                        # Music
                                        elif optionsSelect == 2:
                                            if musicEnabled:
                                                musicEnabled = False
                                                pygame.mixer.music.set_volume(0)
                                            else:
                                                musicEnabled = True
                                                pygame.mixer.music.set_volume(0.2)
                                        # SFX
                                        elif optionsSelect == 3:
                                            if sfxEnabled:
                                                sfxEnabled = False
                                                muteSfx()
                                            else:
                                                sfxEnabled = True
                                                unMuteSfx()

                    # Controls Menu
                    elif menuSelect == 2:
                        inControls = True
                        while inControls:
                            drawMainMenu()
                            clock.tick(FPS)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    quitGame = True
                                    inControls = False
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                                        inControls = False
                                        audioCancel.play()
                    elif menuSelect == 3:
                        quitGame = True
                        inMenu = False

    # Game Start
    # Spawn/create players
    p1 = Player(WIDTH/2 * 1.5 - PLAYER_WIDTH/2, 2*HEIGHT - GROUND - PLAYER_HEIGHT,"white")
    p2 = Player(WIDTH/4 - PLAYER_WIDTH/2, 2*HEIGHT - GROUND - PLAYER_HEIGHT,"red")

    frame = 1
    ROUND_START = time.time()
    timeLimit = 120
    elapsed = 0
    timeLeft = timeLimit
    
    # Skip game loop if user exited in menu
    if quitGame:
        inPlay = False
        inGame = False
    else:
        inPlay = True
    
    debugMode = False
    gameOver = False

#---------------------------------------#
# Main Game Loop                        #
#---------------------------------------#
    while inPlay:

        drawGameWindow()
        clock.tick(FPS)
        
        if p1.hp <= 0 or p2.hp <= 0:
            gameOver = True

        # Round Timer
        frame = (frame + 1) % 60  # Debug purposes
        if timerEnabled and not gameOver:
            elapsed = int(time.time() - ROUND_START)
            if timeLeft > 0:
                timeLeft = timeLimit - elapsed
            if timeLeft == 0:
                gameOver = True

        # Movement input
        keys = pygame.key.get_pressed()

        ### PLAYER 1 ### (right side)
        # Crouch
        if keys[pygame.K_DOWN] and p1.isJumping is False:
            if p1.playerState == 0:
                p1.isCrouching = True
        elif p1.playerState == 0:
            p1.isCrouching = False
        
        if keys[pygame.K_LEFT] and p1.isJumping is False:  
            p1.move(0)     # Move left
        elif keys[pygame.K_RIGHT] and p1.isJumping is False:
            p1.move(1)     # Move right
        else:
            p1.isMoving = False
        
        #### PLAYER 2 ### (left side)
        # Crouch
        if keys[pygame.K_s] and p2.isJumping is False:
            if p2.playerState == 0:
                p2.isCrouching = True
        elif p2.playerState == 0:
            p2.isCrouching = False
        # Move left
        if keys[pygame.K_a] and p2.isJumping is False:
            p2.move(0)
        # Move right
        elif keys[pygame.K_d] and p2.isJumping is False:
            p2.move(1)
        else:
            p2.isMoving = False

        # Jump input is in a seperate loop to prevent flying and because it requires keydown
        # Dash input is also here, as it requires two consecutive keydowns
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
                inGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    audioCancel.play()
                    inPlay = False
                    inMenu = True
                if event.key == pygame.K_UP and p1.posY + PLAYER_HEIGHT == GROUND:
                    p1.jump()
                if event.key == pygame.K_w and p2.posY + PLAYER_HEIGHT == GROUND:
                    p2.jump()
                if event.key == pygame.K_LEFT:
                    p1.moveInputList.append(0)
                if event.key == pygame.K_RIGHT:
                    p1.moveInputList.append(1)
                if event.key == pygame.K_a:
                    p2.moveInputList.append(0)
                if event.key == pygame.K_d:
                    p2.moveInputList.append(1)
                if event.key == pygame.K_KP1:
                    p1.attack(0)
                if event.key == pygame.K_KP2:
                    p1.attack(1)
                if event.key == pygame.K_t:
                    p2.attack(0)
                if event.key == pygame.K_y:
                    p2.attack(1)
                if event.key == pygame.K_g:
                    audioMenuMove.play()
                    if debugMode:
                        debugMode = False
                    else:
                        debugMode = True
        
        # Update and move characters
        p2.update(p1)
        p1.update(p2)

        p1.attackHitbox.deSpawn(p1)  # despawns hitboxes
        p2.attackHitbox.deSpawn(p2)

        p1.checkWindup()
        p2.checkWindup()  # spawns hitboxes

pygame.quit()
