class Striker:
    def.__init__(self,posx, posy,width,height,speed,color):
        self.posx, self.posy=posx, posy
        self.width,self.height=width, pygame.freetype.height
        self.speed= speed
        self.color= color 

        self.strikerRect= pygame.Rect(self.posx, self.posy,self.width.self.height)
        self.striker=pygame.draw.rect(screen, self.color, self.strikerRect)
    
def display(self):
    sef.striker= pygame.draw.rect(screen, self.color, self.strickerRect)

#used to update the state of the object
def update(self,xFac):
    self.posx += self.speed*xFac

    #restricting the striker to be in between\
    #  the left and right edges of screen

    if self.posx <=0:
        self.posx= 0
    elif self.posx+self.width >=WIDTH:
        self.posx= WIDTH-self.width
    
    self.strikerRect= pygame.Rect(
        self.posx,self.posy, self.width, self.height
    )
#return the rect of the object
def getTect(self):
    return self.strikerRect
