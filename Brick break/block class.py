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
        self.blockRect=pygame. Rect( self.posx, self posy, self.width, self.height)
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