#########################################
# Filename: FinalGameClasses.py
# Description: Final Game classes version 2
# Author: Sunny Jiao
# Date: 01/13/19
#########################################

import pygame

# All game constants (e.g. width, height, colours, gravity, playersize, etc. are located in this class)
from FinalGameSettings import *

class FrameTimer(object):
    """ Frame counter object
        Uses incrementing frames to create timers for the game delays
        e.g. attack delay, dash delay, stun delay, etc.
    """
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        
    def reset(self):
        self.count = 0

    def increment(self, amount=1):
        self.count += amount
        
    def timeUp(self):
        if self.count >= self.limit:
            return True
        return False


class Sprite(object):

    def __init__(self, colour):
        
        self.solaireWalking = [0] * 4
        self.solaireDashing = [0] * 3
        self.solaireDashingBack = [0] * 3
        self.solaireNLight = [0] * 3
        self.solaireNHeavy = [0] * 3
        self.solaireCLight = [0] * 3
        self.solaireCHeavy = [0] * 4
        self.solaireJLight = [0] * 3
        self.solaireJHeavy = [0] * 2
        self.solaireCrouch = [0] * 2
        self.solaireHurt = [0] * 3
        self.solaireBlock = [0] * 3

        for i in range(4):
            self.solaireWalking[i] = pygame.image.load("img/solaire"+colour+"/walk" + str(i) + ".png").convert_alpha()
            self.solaireCHeavy[i] = pygame.image.load("img/solaire"+colour+"/cheavy" + str(i) + ".png").convert_alpha()

        for i in range(3):
            self.solaireNLight[i] = pygame.image.load("img/solaire"+colour+"/nlight" + str(i) + ".png").convert_alpha()
            self.solaireNHeavy[i] = pygame.image.load("img/solaire"+colour+"/nheavy" + str(i) + ".png").convert_alpha()
            self.solaireCLight[i] = pygame.image.load("img/solaire"+colour+"/clight" + str(i) + ".png").convert_alpha()
            self.solaireJLight[i] = pygame.image.load("img/solaire"+colour+"/jlight" + str(i) + ".png").convert_alpha()
            self.solaireHurt[i] = pygame.image.load("img/solaire"+colour+"/hurt" + str(i) + ".png").convert_alpha()
            self.solaireBlock[i] = pygame.image.load("img/solaire"+colour+"/block" + str(i) + ".png").convert_alpha()

        for i in range(2):
            self.solaireCrouch[i] = pygame.image.load("img/solaire"+colour+"/crouch" + str(i) + ".png").convert_alpha()
            self.solaireJHeavy[i] = pygame.image.load("img/solaire"+colour+"/jheavy" + str(i) + ".png").convert_alpha()

        self.solaireJump = [pygame.image.load("img/solaire"+colour+"/jump0.png").convert_alpha()]
        self.solaireIdle = [pygame.image.load("img/solaire"+colour+"/idle0.png").convert_alpha()]
        self.solaireDashing = [pygame.image.load("img/solaire"+colour+"/dash0.png").convert_alpha()]
        self.solaireDashingBack = [pygame.image.load("img/solaire"+colour+"/dashback0.png").convert_alpha()]
        self.solaireDead = [pygame.image.load("img/solaire"+colour+"/dead0.png").convert_alpha()]


class AttackHitbox(object):
    """
        Rect object with health and attack attributes,
        and spawn/despawn methods
    """

    def __init__(self, attackType):
        if attackType == "Nlight" or attackType == "Clight" or attackType == "Jlight":
            self.rect = pygame.Rect(-hitboxOffset, -hitboxOffset, 103, 40)
            self.attackPower = 2
            
        elif attackType == "Nheavy":
            self.rect = pygame.Rect(-hitboxOffset, -hitboxOffset, 110, 100)
            self.attackPower = 4

        elif attackType == "Jheavy":
            self.rect = pygame.Rect(-hitboxOffset, -hitboxOffset, 85, 70)
            self.attackPower = 6
        
        elif attackType == "Cheavy":
            self.rect = pygame.Rect(-hitboxOffset, -hitboxOffset, 120, 160)
            self.attackPower = 7

    def spawn(self, player):
        if player.faceDirection == 1:
            if player.attackType == "Nheavy":
                audioHeavySwing.play()
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset, player.posY + hitboxOffset + 50)
            elif player.attackType == "Jlight":
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset, player.posY + hitboxOffset + 125)
                audioKick.play()
            elif player.attackType == "Jheavy":
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset - 55, player.posY + hitboxOffset + 120)
                audioDive.play()
            elif player.attackType == "Clight":
                audioLightSwing.play()
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset, player.posY + hitboxOffset + 75)
            elif player.attackType == "Cheavy":
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset, player.posY + hitboxOffset - 30)
                audioLargeHit.play()
            else:
                audioLightSwing.play()
                self.rect = self.rect.move(player.posX + PLAYER_WIDTH + hitboxOffset, player.posY + hitboxOffset + PLAYER_HEIGHT/4)
        else:
            if player.attackType == "Nheavy":
                audioHeavySwing.play()
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset, player.posY + hitboxOffset + 50)
            elif player.attackType == "Jlight":
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset, player.posY + hitboxOffset + 125)
                audioKick.play()
            elif player.attackType == "Jheavy":
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset + 55, player.posY + hitboxOffset + 120)
                audioDive.play()
            elif player.attackType == "Clight":
                audioLightSwing.play()
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset, player.posY + hitboxOffset + 75)
            elif player.attackType == "Cheavy":
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset, player.posY + hitboxOffset - 30)
                audioLargeHit.play()
            else:
                audioLightSwing.play()
                self.rect = self.rect.move(player.posX - self.rect.width + hitboxOffset, player.posY + PLAYER_HEIGHT/4 + hitboxOffset)
    
    def deSpawn(self, player):
        self.rect = pygame.Rect(-hitboxOffset, -hitboxOffset, player.attackHitbox.rect.width, player.attackHitbox.rect.height)


class Player(object):

    """ Player-controlled character object
        Attributes:
            bodyHitbox - Rect object
            attackHitbox - Rect object
            bodyX - bodyHitbox x coordinate
            bodyY - bodyHitbox y coordinate
            playerState
                0 : idle/moving
                1 : attacking
                2 : hurt
                3 : dashing
                4 : hurt but blocking

            attackInputList = list of inputs
            inputFrameLimit - frame counter for inputs
            hurtFrameCount - frame counter for getting hurt
            inputType - light or strong attack
                0 : light attack
                1 : strong attack

            canAttack - boolean
            isHurt - boolean
            isJumping - boolean

            hp - health points
            charge - special move charge meters
            faceDirection - int - facing left/right
                0 : facing left
                1 : facing right

        behaviour:
            moveLeft()
            moveRight()
            attack()
            update()
            jump()
            getHurt()
    """

    def __init__(self, x, y, colour):
        self.posX = x
        self.posY = y
        self.velX = 0
        self.velY = 0

        self.colour = colour
        self.picNum = 0
        self.spriteDelayCount = 0
        self.sprite = Sprite(self.colour)

        self.hpPast = 100
        self.hp = 100
        self.charge = 0
        self.playerState = 0
        self.attackInputList = []
        self.moveInputList = []
        self.attackSpriteList = []
        self.attackSpriteListIterator = 0
        self.attackType = "Nlight"
        self.knockbackY = 0
        self.knockbackX = 0.2
        self.knocked = False

        self.isMoving = False
        self.isJumping = False
        self.isCrouching = False
        self.isBlocking = False
        self.canAttack = True
        self.inWindup = False

        self.faceDirection = 1
        self.moveDirection = 0
        self.dashDirection = 0

        self.attackWindup = FrameTimer(3)
        self.attackDelay = FrameTimer(7)
        self.comboDelay = FrameTimer(24)
        self.moveInputTimer = FrameTimer(13)
        self.dashTimer = FrameTimer(12)
        self.stunTimer = FrameTimer(10)
        self.walkCount = 0
        
        self.blockHitbox = pygame.Rect(-200, -200, PLAYER_WIDTH/4, PLAYER_HEIGHT)
        self.bodyHitbox = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.attackHitbox = AttackHitbox("Nlight")

    def drawSprite(self):
        
        ### ASSINGING SPRITES ###
        # Attack Sprites
        if self.playerState == 1:
            if self.attackType == "Nlight" and self.canAttack is False:
                self.spriteCurrentList = self.sprite.solaireNLight
                self.attackSpriteListIterator += 1
          
            elif self.attackType == "Nheavy":
                self.spriteCurrentList = self.sprite.solaireNHeavy
                self.attackSpriteListIterator += 1

            elif self.attackType == "Clight" and self.canAttack is False:
                self.spriteCurrentList = self.sprite.solaireCLight
                self.attackSpriteListIterator += 1

            elif self.attackType == "Cheavy" and self.canAttack is False:
                self.spriteCurrentList = self.sprite.solaireCHeavy
                self.attackSpriteListIterator += 1

            elif self.attackType == "Jlight" and self.canAttack is False:
                self.spriteCurrentList = self.sprite.solaireJLight
                self.attackSpriteListIterator += 1

            elif self.attackType == "Jheavy":
                self.spriteCurrentList = self.sprite.solaireJHeavy
                self.attackSpriteListIterator += 1

            self.picNum = self.attackSpriteList[self.attackSpriteListIterator]
    
        # Hurt Sprite
        elif self.playerState == 2:
            self.spriteCurrentList = self.sprite.solaireHurt
            if self.isCrouching:
                self.picNum = 1
            elif self.isJumping:
                self.picNum = 2
            else:
                self.picNum = 0
        
        # Block Sprite
        elif self.playerState == 4:
            self.spriteCurrentList = self.sprite.solaireBlock
            if self.isCrouching:
                self.picNum = 1
            elif self.isJumping:
                self.picNum = 2
            else:
                self.picNum = 0

        # Dead sprite
        elif self.playerState == 5:
            self.spriteCurrentList = self.sprite.solaireDead
            self.picNum = 0

        # Dashing Sprite
        elif self.playerState == 3:
            if self.moveDirection == 1 and self.faceDirection == 1 or self.moveDirection == 0 and self.faceDirection == 0:
                self.spriteCurrentList = self.sprite.solaireDashing
            else:
                self.spriteCurrentList = self.sprite.solaireDashingBack
            self.picNum = 0

        # Crouch Sprite
        elif self.isCrouching:
            self.spriteCurrentList = self.sprite.solaireCrouch
            self.spriteDelayCount += 1
            if self.spriteDelayCount <= 2:
                self.picNum = 0
            else:
                self.picNum = 1
        
        # Jumping sprite
        elif self.isJumping:
            self.spriteCurrentList = self.sprite.solaireJump
            self.picNum = 0

        # Walking sprite
        elif self.isMoving:
            self.spriteCurrentList = self.sprite.solaireWalking
            if self.moveDirection == 1:
                self.spriteDelayCount = (self.spriteDelayCount + 1) % 32
                self.picNum = self.spriteDelayCount / 8
            elif self.moveDirection == 0:
                self.spriteDelayCount = (self.spriteDelayCount + 1) % 32
                self.spriteDelayCountTemp = 31 - self.spriteDelayCount
                self.picNum = self.spriteDelayCountTemp / 8

        else:
            self.picNum = 0
            self.spriteDelayCount = 0
            self.spriteDelayCountTemp = 0
            self.attackSpriteListIterator = 0
            self.spriteCurrentList = self.sprite.solaireIdle

        ### BLITING SPRITES ###
        if self.faceDirection == 1:
            gameWindow.blit(self.spriteCurrentList[self.picNum], (self.posX - SPRITE_X_OFFSET, self.posY - SPRITE_Y_OFFSET))
        else:
            gameWindow.blit(pygame.transform.flip(self.spriteCurrentList[self.picNum], True, False), (self.posX - SPRITE_X_OFFSET, self.posY - SPRITE_Y_OFFSET))

    def move(self, direction):
        if not self.isCrouching:
            self.walkCount = (self.walkCount + 1) % 25
            if self.walkCount == 24:
                audioStep.play()

        self.moveDirection = direction
        if self.playerState == 0:
            self.isMoving = True
            if not self.isCrouching:
                if self.moveDirection == 0:
                    self.velX = -PLAYER_X_SPEED
                elif self.moveDirection == 1:
                    self.velX = PLAYER_X_SPEED

    def jump(self):
        if self.playerState == 0:
            self.velY = JUMP_SPEED
            self.isJumping = True
            audioJump.play()

    def dash(self):
        if self.playerState == 0 and not self.isCrouching:
            self.playerState = 3
            self.moveInputList = []
            self.moveInputTimer.reset()
            audioDash.play()

    def checkWindup(self):
        if self.attackWindup.timeUp():
            self.attackHitbox.spawn(self)
            self.attackWindup.reset()
            self.inWindup = False

    def getHurt(self, enemy):
        self.playerState = 2
        self.canAttack = False
        self.hp = self.hp - enemy.attackHitbox.attackPower
        self.hpPast = self.hp + enemy.attackHitbox.attackPower
            
        if enemy.attackType == "Cheavy":
            self.velY = JUMP_SPEED
            self.knocked = True
        
        if self.hp <= 0:
            audioDeath.play()

    def block(self, enemy):
        self.playerState = 4
        self.canAttack = False
        self.hp = self.hp - enemy.attackHitbox.attackPower * 0.3
        self.hpPast = self.hp + enemy.attackHitbox.attackPower * 0.3

    def attack(self, inputType):
        """
            - Attacks have two major attributes: Combo timer and attack delay timer.
            - Combo timer determines which inputs will be strung together into a combo input.
            - Delay timer seperates each individual input prevents the player from spamming attacks.
            - When the combo timer is up, the player will exit the attacking state (playerState = 0).
            - The delay timer alters the bool canAttack, which can toggle on or off while player is in attacking state.
            - As well, each attack has a windup timer, which creates a delay between the player hitting the attack
            key and the character's hitbox spawning.
        """
        if self.canAttack:
            
            self.playerState = 1
            self.comboDelay.reset()
            self.attackDelay.limit = 15
            self.attackInputList.append(inputType)

            # Assigning appropriate attack hitboxes (size and damage)
            self.attackHitbox = AttackHitbox(inputType)

            self.inWindup = True

            ### Spawning attack hitboxes and combos ###
            
            # Normal light / Jumping light / Crouching light
            if self.attackInputList == [0] or self.attackInputList == [0,0]:
                if self.isJumping:
                    self.attackType = "Jlight"
                elif self.isCrouching:
                    self.attackType = "Clight"
                else:
                    self.attackType = "Nlight"
                self.attackDelay.limit = 9
                self.attackWindup.limit = 4
                self.attackSpriteList = [0,0,0,0,1,1,1,1,2,2,2,2,2]

            # Triple light / Triple crouching light
            if self.attackInputList == [0,0,0]:
                if self.isCrouching:
                    self.attackType = "Clight"
                else:
                    self.attackType = "Nlight"
                self.comboDelay.reset()
                self.attackDelay.limit = 16
                self.attackInputList = []
                self.attackWindup.limit = 5
                self.attackSpriteList = [0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,2]

            # Crouching heavy
            if (self.attackInputList == [1] or self.attackInputList == [0,1] or self.attackInputList == [0,0,1]) and self.isCrouching:
                self.attackType = "Cheavy"
                self.comboDelay.reset()
                self.attackDelay.limit = 42
                self.attackInputList = []
                self.attackWindup.limit = 15
                self.attackSpriteList = [0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
                audioLargePullout.play()

            # Jumping Heavy
            elif self.attackInputList == [1] and self.isJumping:
                self.attackType = "Jheavy"
                self.comboDelay.reset()
                self.attackDelay.limit = 24
                self.attackInputList = []
                self.attackWindup.limit = 8
                self.attackSpriteList = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

            # Normal heavy
            elif self.attackInputList == [1] or self.attackInputList == [0,1] or self.attackInputList == [0,0,1]:
                self.attackType = "Nheavy"
                self.comboDelay.reset()
                self.attackDelay.limit = 24
                self.attackInputList = []
                self.attackWindup.limit = 8
                self.attackSpriteList = [0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
          
            self.attackSpriteListIterator = 0
            self.attackDelay.reset()
            self.attackHitbox = AttackHitbox(self.attackType)
            self.canAttack = False
    
    def update(self, enemy):

        ### UPDATE MOVEMENT ###

         # Update Y velo
        self.velY += GRAVITY

        # Jumping velocity
        if self.isJumping:
            if self.isMoving:
                self.diagJump = True
            if self.diagJump:
                if self.moveDirection == 0:
                    self.velX = -PLAYER_X_SPEED
                elif self.moveDirection == 1:
                    self.velX = PLAYER_X_SPEED
          
        # Move player and body hitbox
        self.posX += self.velX
        self.posY += self.velY
        self.bodyHitbox.bottomleft = (self.posX, self.posY + PLAYER_HEIGHT)
        
        ### RESET MOVEMENT STATUSES ###

        # Jumping
        if self.posY + PLAYER_HEIGHT >= GROUND:
            self.isJumping = False
            self.diagJump = False
            self.velY = 0

        # Reset X Velo
        if self.isJumping is False:
            self.velX = 0

        # Make characters stand on the ground
        if self.posY + PLAYER_HEIGHT >= GROUND:
            self.posY = GROUND - PLAYER_HEIGHT

        # Make characters stay on screen
        if self.posX < 0:
            self.posX = 0
        elif self.posX > WIDTH - PLAYER_WIDTH:
            self.posX = WIDTH - PLAYER_WIDTH

        # Face Direction
        if self.playerState != 5:  # If dead, player will not switch directions
            if self.posX > enemy.posX:
                self.faceDirection = 0
            else:
                self.faceDirection = 1

        ### DETECTIONS ###

        # If Crouching
        if self.isCrouching:
            if self.playerState == 0 or self.playerState == 1:
                self.bodyHitbox = pygame.Rect(self.posX, self.posY + PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT/2)
        else:
            self.bodyHitbox = pygame.Rect(self.posX, self.posY, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Detect Blocking
        if (self.moveDirection != self.faceDirection) and (self.isMoving or self.isJumping) and (self.playerState == 0 or self.playerState == 4):
            self.isBlocking = True
        else:
            self.isBlocking = False
        
        # If blocking
        if self.isBlocking:
            if self.faceDirection == 0:
                self.blockHitbox = pygame.Rect(self.bodyHitbox.left - 10, self.bodyHitbox.top, PLAYER_WIDTH/4, PLAYER_HEIGHT)
            else:
                self.blockHitbox = pygame.Rect(self.bodyHitbox.left + PLAYER_WIDTH - 10, self.bodyHitbox.top, PLAYER_WIDTH/4, PLAYER_HEIGHT)
        else:
            self.blockHitbox = pygame.Rect(-200, -500, PLAYER_WIDTH, PLAYER_HEIGHT)
        
        # Detect collision between players
        # Attack blocked -> attack hitbox collides with block hitbox
        if self.blockHitbox.colliderect(enemy.attackHitbox):
            self.block(enemy)
            audioShield.play()
        # Attack not blocked -> attack hitbox doesn't collide with block hitbox, does collide with body hitboxs
        elif self.bodyHitbox.colliderect(enemy.attackHitbox):
            self.getHurt(enemy)
            audioHurt.play()

        # If hurt -> playerState 2
        if self.playerState == 2:
            self.stunTimer.limit = 30
            self.stunTimer.increment()
            # Knocked bool is uniquly activated by the Crouching Heavy attack, which
            # will launch the enemy further horizontally than other attacks, and also
            # launch the enemy up vertically.
            # Vertical launch is in the getHurt() function, as jumping is a one-time activation mechanic unlike X movement
            if self.knocked:
                if self.faceDirection == 1:
                    self.velX = -PLAYER_X_SPEED * 2
                else:
                    self.velX = PLAYER_X_SPEED * 2
            
            # X knockback for normal attacks
            elif self.faceDirection == 1:
                self.velX = -PLAYER_X_HIT_SPEED
            else:
                self.velX = PLAYER_X_HIT_SPEED
            
            if self.stunTimer.timeUp():
                self.playerState = 0
                self.stunTimer.reset()
                self.canAttack = True
        else:
            self.knocked = False
            
        # Check if dead
        if self.hp <= 0:
            self.playerState = 5

        # If blocked attack -> playerState 4
        if self.playerState == 4:
            self.stunTimer.limit = 10
            self.stunTimer.increment()
            if self.stunTimer.timeUp():
                self.playerState = 0
                self.stunTimer.reset()
                self.canAttack = True

        # If attacking -> playerState 1
        if self.canAttack is False:
                self.attackDelay.increment()
        
        if self.playerState == 1:
            if self.inWindup:
                self.attackWindup.increment()

            self.comboDelay.increment()

            # Reset attack delay
            if self.attackDelay.timeUp():
                self.canAttack = True
                self.attackDelay.reset()
            
            # Reset combo timer
            if self.attackInputList == []:
                self.comboDelay.count = 0
            if self.comboDelay.timeUp():
                self.attackInputList = []  # Clear inputs if attack is not within combo time
                self.comboDelay.reset()

            if self.comboDelay.count == 0 and self.attackDelay.count == 0:
                self.playerState = 0
                self.canAttack = True
                self.attackDelay.reset()
        
        # If player is not attacking, data can be cleared
        else:
            self.attackInputList = []
            self.comboDelay.reset()
            self.attackType = "none"

        # Dash detect
        if len(self.moveInputList) != 0:
            self.moveInputTimer.increment()
            if len(self.moveInputList) == 2:
                if (self.moveInputList == [0,0] or self.moveInputList == [1,1]) and self.moveInputTimer.timeUp() is False:
                    self.dashDirection = self.moveInputList[0]
                    self.dash()
                else:
                    self.moveInputList = []
                    self.moveInputTimer.reset()
            if self.moveInputTimer.timeUp():
                self.moveInputList = []
                self.moveInputTimer.reset()
        
        # if Dashing -> playerState 3
        if self.playerState == 3:
            self.dashTimer.increment()
            if self.dashTimer.timeUp() is False:
                if self.dashDirection == 1:
                    self.velX = PLAYER_DASH_SPEED
                elif self.dashDirection == 0:
                    self.velX = -PLAYER_DASH_SPEED
            else:
                self.dashTimer.reset()
                self.playerState = 0
