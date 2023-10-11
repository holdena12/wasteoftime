import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()
#set up screen
windowy=750
windowx=1250
objectsizey = 50
objectsizex = 93

trashsizex = windowx /3
trashsizey = windowy /5
trashimg = pygame.image.load("Trash.png")
objectimg = pygame.image.load("Clock.png")
trashimg = pygame.transform.scale(trashimg,(trashsizex,trashsizey))
objectimg = pygame.transform.scale(objectimg,(objectsizex,objectsizey))
screen = pygame.display.set_mode([windowx,windowy])
trashx = (windowx - trashsizex)/2
trashy = windowy - trashsizey
down_pressed = False

score = 0
minSpeed = 3
maxSpeed = 5
pygame.display.set_caption('Waste of Time')
font = pygame.font.Font('freesansbold.ttf', 32)
vel = 3
fallingvel = 5
gameover = False
 
class FlyingClock:
    x = 0
    y = 0
    direction = 0
   

    def __init__(self):
        self.y = windowy/2
        rand = random.randint(0,1)
        if rand == 1:
            self.x = 0
            self.direction = 1
        else:
            self.x = windowx
            self.direction = -1
    
    def updateXPostion(self, vel):
        self.x = self.x + (vel * self.direction)
    
    def moveDown(self,fallingvel):
        self.y = self.y + fallingvel

    def draw(self):
        if gameover == False:
            screen.blit(objectimg,(self.x,self.y))
   

    

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
level = 1
# create a text surface object,
# on which text is drawn on it.
text = font.render('', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (0, 25)

time = 0
def printObjectData(flyingClock):
    print("TrasCan: ", trashx, ",", trashy, " object: ", flyingClock.x, ",", flyingClock.y)
def triggerGameOver(minSpeed,maxSpeed,fallingVel):
        screen.fill((0,0,0))
        text2 = font.render('GaMe OvEr', True,(255,0,0))
        textRect2 = text2.get_rect()
        textRect2.center = (windowx // 2, windowy // 2)
        screen.blit(text2,textRect2)
        screen.blit(text,textRect)
        minSpeed = 3
        maxSpeed = 5

        fallingvel = 5
        gameover = True
# runs the end game logic
def checkGameOver(flyingClock):
    

        
    
    if flyingClock.direction == 1 and flyingClock.y > windowy:
        triggerGameOver(minSpeed,maxSpeed, fallingvel)
        return True
    
        
    if flyingClock.x < 0 or flyingClock.y > windowy:
        triggerGameOver(minSpeed,maxSpeed,fallingvel)
        return True
    
    return False
text3 = font.render('Level: {level} ', True,(255,0,0))
textRect3 = text3.get_rect()
textRect3.center = (25 , windowx - 100)
screen.blit(text3,textRect3)
#game loop
loopCount = 0
flyingClock = FlyingClock()
def increase_game_speed(minSpeed,maxSpeed,fallingvel):
    minSpeed = minSpeed+3
    maxSpeed = maxSpeed+3
    fallingvel = fallingvel+3
def levelup(level):
    if score % 5 == 0:
        level += 1
        increase_game_speed(minSpeed,maxSpeed,fallingvel)

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
             pygame.display.quit(), sys.exit()
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              down_pressed = True
        if gameover == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    down_pressed = False
                    gameover = False
                    time = 0
                    flyingClock = FlyingClock()
                    score = 0
                    minSpeed = 3
                    maxSpeed = 5
                    fallingvel = 5


    if gameover == True:
        continue
    
    #TODO: change this to a function.  check to see if clock is thrown away
    if flyingClock.x > trashx and flyingClock.x < trashx +trashsizex and flyingClock.y > trashy and flyingClock.y < trashy + trashsizey:
        score +=1
        print(score)
        down_pressed = False
        flyingClock = FlyingClock()
        levelup(level)
        #TODO: this should be a member variable of FlyingClock
        
       # minSpeed = minSpeed * 1.2
       # maxSpeed = maxSpeed * 1.2
       # fallingvel = fallingvel * 1.1
        minSpeed = int(minSpeed)
        maxSpeed = int(maxSpeed)
        vel = random.randint(minSpeed,maxSpeed)
        if vel < 3:
            vel = 3
    if flyingClock.direction == 1:
        if flyingClock.y > windowy:
            checkGameOver(flyingClock)
    if down_pressed == True:
        flyingClock.moveDown(fallingvel)
    else:
        flyingClock.updateXPostion(vel)
    
    time = time+0.01
    
    if checkGameOver(flyingClock) == False:
        screen.fill((0,0,225))
        if loopCount % 100 == 0:
            printObjectData(flyingClock)
            loopCount += 1
        timeStr = "%.2f" % time
        text = font.render(timeStr,True,(255,255,255))
        screen.blit(text,textRect)
        flyingClock.draw()
        screen.blit(trashimg,(trashx,trashy))
    else:
        gameover = True
        checkGameOver(flyingClock)
    pygame.display.flip()
    clock.tick(100)
        