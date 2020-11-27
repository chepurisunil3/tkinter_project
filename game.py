import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("Test")
gameExit = False
def_x = 300
def_y = 300
def_x_change = 0
def_y_change = 0
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                def_x_change = -1
                def_y_change = 0
            if event.key == pygame.K_RIGHT:
                def_x_change = 1
                def_y_change = 0
            if event.key == pygame.K_DOWN:
                def_y_change = 1
                def_x_change = 0
            if event.key == pygame.K_UP:
                def_y_change = -1
                def_x_change = 0
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         def_x_change = 0
        #         def_y_change = 0
        #     if event.key == pygame.K_RIGHT:
        #         def_x_change = 0
        #         def_y_change = 0
        #     if event.key == pygame.K_DOWN:
        #         def_y_change = 0
        #         def_x_change = 0
        #     if event.key == pygame.K_UP:
        #         def_y_change = 0
        #         def_x_change = 0
    def_x += def_x_change   
    def_y += def_y_change
    gameDisplay.fill((255,255,255))
    pygame.draw.rect(gameDisplay,(0,0,0),[def_x,def_y,50,50]) # x,y,x-size,y-size
    gameDisplay.fill((255,0,0),rect=[0,0,50,50])
    pygame.display.update()
    clock.tick(30)


