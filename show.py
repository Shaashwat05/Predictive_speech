import pygame

def show_init():
    pygame.init()

    screen_size=(800, 600)
    screen=pygame.display.set_mode(screen_size)

    pygame.display.set_caption('Show speech') 

    return screen

def paint(screen, txt, posx, posy):
    clock = pygame.time.Clock()

    green = (0, 255, 0) 

    font = pygame.font.Font('freesansbold.ttf', 18) 

    text = font.render(txt, True, green) 
    
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect() 
    if((posx + textRect[2]) <= 800):
        textRect = textRect.move(posx, posy)
    else:
        posy +=textRect[3]
        posx = 0
        textRect = textRect.move(posx, posy)
        #posx += textRect[2]

    pygame.display.update()
    
    for i in range(len(txt)):
            text2 = font.render(txt[i], True, green) 
            screen.blit(text2, (posx +(font.size(txt[:i])[0]), posy)) 
            pygame.display.update()
            clock.tick(12)
    

    #if(count == 1):
    posx += textRect[2]
    
    return posx, posy



def pred_show(screen, txt, posx, posy):

    green = (0, 255, 0) 
    blue = (0, 0, 128) 

    font = pygame.font.Font('freesansbold.ttf', 18) 

    text = font.render(txt, True, green, blue) 
    
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect() 
    if((posx + textRect[2]) <= 800):
        textRect = textRect.move(posx, posy)
    else:
        textRect = textRect.move(0, posy + textRect[3])
        #posx += textRect[2]
    pygame.display.update()
    
    # infinite loop 
    disp = True
    screen.blit(text, (posx, posy)) 
    '''
    while disp : 
        
    
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 

                pygame.quit() 
    
                quit() 
    
            pygame.display.update()  
            break
        disp = False'''


'''

screen = show_init()
posx = 0
posy = 0
for i in range(7):
    print(str(posx)+ "   " + str(posy))
    text = "My name is shaashwat and i am awesome" + str(i)
    posx, posy = paint(screen, text, posx, posy)'''



