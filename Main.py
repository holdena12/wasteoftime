import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()
#set up screen
windowy=1000
windowx=1500
objectsizey = 50
objectsizex = 93


trashimg = pygame.image.load("Trash.png")
objectimg = pygame.image.load("Clock.png")
objectimg = pygame.transform.scale(objectimg,(objectsizex,objectsizey))
screen = pygame.display.set_mode([windowx,windowy])
trashx = 550
trashy = 800
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
        self.y = 350
        rand = random.randint(0,1)
        if rand == 1:
            self.x = 0
            self.direction = 1
        else:
            self.x = 1475
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

# runs the end game logic
def isGameOver(flyingClock):
    if flyingClock.x <0 or flyingClock.y > 1000:
        screen.fill((0,0,0))
        text2 = font.render('GaMe OvEr', True,(255,0,0))
        textRect2 = text2.get_rect()
        textRect2.center = (windowx // 2, windowy // 2)
        screen.blit(text2,textRect2)
        screen.blit(text,textRect)
        gameover = True
        return True
    else:
        return False

#game loop
loopCount = 0
flyingClock = FlyingClock()

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
             pygame.display.quit(), sys.exit()
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
              down_pressed = True
        if gameover == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    down_pressed = False
                    gameover = False
                    time = 0
                    flyingClock = FlyingClock()


    if gameover == True:
        continue
    
    #TODO: change this to a function.  check to see if clock is thrown away
    if flyingClock.x > trashx and flyingClock.x < trashx +400 and flyingClock.y > trashy and flyingClock.y < trashy + 200:
        score +=1
        print(score)
        down_pressed = False
        flyingClock = FlyingClock()
        #TODO: this should be a member variable of FlyingClock
        
        minSpeed = minSpeed * 1.2
        maxSpeed = maxSpeed * 1.2
        fallingvel = fallingvel * 1.1
        minSpeed = int(minSpeed)
        maxSpeed = int(maxSpeed)
        vel = random.randint(minSpeed,maxSpeed)
        if vel < 3:
            vel = 3
         
    if down_pressed == True:
        flyingClock.moveDown(fallingvel)
    else:
        flyingClock.updateXPostion(vel)
    
    time = time+0.01
    
    if isGameOver(flyingClock) == False:
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
        isGameOver(flyingClock)
    pygame.display.flip()
    clock.tick(100)
        