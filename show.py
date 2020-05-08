import pygame


def show_init():
    pygame.init()

    screen_size=(600, 800)
    screen=pygame.display.set_mode(screen_size)

    pygame.display.set_caption('Show speech') 

    return screen

def paint(screen, text):
    green = (0, 255, 0) 
    blue = (0, 0, 128) 

    font = pygame.font.Font('freesansbold.ttf', 24) 

    text = font.render(text, True, green, blue) 
    
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
    
    # set the center of the rectangular object. 
    textRect.center = (600 // 2, 800 // 2) 
    
    # infinite loop 
    while True : 

        screen.blit(text, textRect) 
    
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 

                pygame.quit() 
    
                quit() 
    
            pygame.display.update()  


screen = show_init()

for i in range(2):

    text = "My name is shaashwat and i am awesome"
    paint(screen, text)

