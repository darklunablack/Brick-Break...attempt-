#Fn to check collisions between any 2 entities

def collision_checker(rect,ball):
    if pygame.React.colliderect(rect, ball):
        return True
    
    return False
# fn used to populate the blocks
def populateBlocks (blockWidth, blockHeight, horizontalGap, verticalGap):
    listofBlocks= []

    for i in range(0, Width, blockWidth+horizontalGap):
        for j in range (0,Height//2, blockHeight+verticalGap):
            listofBlocks.append(Block(i,j blockWidth,blockHeight, random.choice([WHITE, GREEN])))
        
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
