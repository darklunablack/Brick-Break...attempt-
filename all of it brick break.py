import pygame
import random

pygame.init()

#Dimension of the screen
WIDTH, HEIGHT = 600, 500

# colors
BLACK= (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED= (255,0,0)

font= pygame.font.Font('freesansbold.ttf', 15)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ('Block Breaker')


#to control the frame rate
clock= pygame.time.Clock()
FPS = 30

#Sticker class
class Striker:
    def __init__(self,posx, posy,width, height,speed,color):
        self.posx, self.posy=posx, posy
        self.width,self.height=width, height
        self.speed= speed
        self.color= color 

        self.strikerRect= pygame.Rect(self.posx, self.posy,self.width, self.height)
        self.striker=pygame.draw.rect(screen, self.color, self.strikerRect)
    
    def display(self):
        self.striker= pygame.draw.rect(screen, self.color, self.strikerRect)

#used to update the state of the object
    def update(self,xFac):
        self.posx += self.speed*xFac

    #restricting the striker to be in between\
    #  the left and right edges of screen

        if self.posx <=0:
            self.posx= 0
        elif self.posx+self.width >=WIDTH:
            self.posx= WIDTH-self.width
    
        self.strikerRect= pygame.Rect(self.posx,self.posy, self.width, self.height)

#return the rect of the object
    def getRect(self):
        return self.strikerRect

class Block:
    def __init__(self,posx,posy,width, height, color):
        self.posx, self.posy =posx, posy
        self.width, self.height= width, height
        self.color= color
        self.damage= 100

        # white blocks have the heath of 200
        #so ball must hit twice to break
        if color== WHITE:
            self.health= 200
        else:
            self.health=100
        
        #the rect variable is used to handle the placement/
        #and collision of the object
        self.blockRect=pygame. Rect( self.posx, self.posy, self.width, self.height)
        self.block=pygame.draw.rect(screen,
                                self.color,self.blockRect)
    
    #used to render object if health is greater that 0
    def display(self):
        if self.health > 0:
            self.brick= pygame.draw.rect(screen, self.color, self.blockRect)
    
    #used to decreased the health of block
    def hit (self):
        self.health -=self.damage
    
    #used to get rect of object
    def getRect(self):
        return self.blockRect
    
    #used to get health from objects
    def getHealth(self):
        return self.health
    

# Ball Class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, 1
          
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
  
    # Used to display the object on the screen
    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
  
    # Used to update the state of the object
    def update(self):
        self.posx += self.xFac*self.speed
        self.posy += self.yFac*self.speed
          
        # Reflecting the ball if it touches either of the vertical edges
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1
  
        # Reflection from the top most edge of the screen
        if self.posy <= 0:
            self.yFac *= -1
  
        # If the ball touches the bottom most edge of the screen, True value is returned
        if self.posy >= HEIGHT:
            return True
  
        return False
  
    # Resets the position of the ball
    def reset(self):
        self.posx = 0
        self.posy = HEIGHT
        self.xFac, self.yFac = 1, -1
  
    # Used to change the direction along Y axis
    def hit(self):
        self.yFac *= -1
  
    # Returns the rect of the ball. In this case, it is the ball itself
    def getRect(self):
        return self.ball

#Fn to check collisions between any 2 entities

def collisionChecker(rect,ball):
    if pygame.Rect.colliderect(rect, ball):
        return True
    
    return False
# fn used to populate the blocks
def populateBlocks (blockWidth, blockHeight, horizontalGap, verticalGap):
        listofBlocks= []

        for i in range(0, WIDTH, blockWidth+horizontalGap):
            for j in range (0,HEIGHT//2, blockHeight+verticalGap):
                listofBlocks.append(Block(i,j, blockWidth,blockHeight, random.choice([WHITE, GREEN])))
        
        return listofBlocks

#All lives over
# until exit or space bar is pressed 
def gameOver():
    gameOver= True
    
    while gameOver:
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True


# Game Manager
def main():
    running = True
    lives = 3
    score = 0
  
    scoreText = font.render("score", True, WHITE)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (20, HEIGHT-10)
  
    livesText = font.render("Lives", True, WHITE)
    livesTextRect = livesText.get_rect()
    livesTextRect.center = (120, HEIGHT-10)
  
    striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE)
    strikerXFac = 0
  
    ball = Ball(0, HEIGHT-150, 7, 5, WHITE)
  
    blockWidth, blockHeight = 40, 15
    horizontalGap, verticalGap = 20, 20
  
    listOfBlocks = populateBlocks(
        blockWidth, blockHeight, horizontalGap, verticalGap)
  
    # Game loop
    while running:
        screen.fill(BLACK)
        screen.blit(scoreText, scoreTextRect)
        screen.blit(livesText, livesTextRect)
  
        scoreText = font.render("Score : " + str(score), True, WHITE)
        livesText = font.render("Lives : " + str(lives), True, WHITE)
  
        # If all the blocks are destroyed, then we repopulate them
        if not listOfBlocks:
            listOfBlocks = populateBlocks(
                blockWidth, blockHeight, horizontalGap, verticalGap)
  
        # All the lives are over. So, the gameOver() function is called
        if lives <= 0:
            running = gameOver()
  
            while listOfBlocks:
                listOfBlocks.pop(0)
  
            lives = 3
            score = 0
            listOfBlocks = populateBlocks(
                blockWidth, blockHeight, horizontalGap, verticalGap)
  
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT:
                    strikerXFac = 1
  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    strikerXFac = 0
  
        # Collision check
        if(collisionChecker(striker.getRect(), ball.getRect())):
            ball.hit()
        for block in listOfBlocks:
            if(collisionChecker(block.getRect(), ball.getRect())):
                ball.hit()
                block.hit()
  
                if block.getHealth() <= 0:
                    listOfBlocks.pop(listOfBlocks.index(block))
                    score += 5
  
        # Update
        striker.update(strikerXFac)
        lifeLost = ball.update()
  
        if lifeLost:
            lives -= 1
            ball.reset()
            print(lives)
  
        # Display
        striker.display()
        ball.display()
  
        for block in listOfBlocks:
            block.display()
  
        pygame.display.update()
        clock.tick(FPS)
if __name__ == "__main__":
    main()
    pygame.quit() 
  
# This code is contributed by teja00219

#game running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False