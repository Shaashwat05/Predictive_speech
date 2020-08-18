import pygame
import time

def show_init(): # initialize pygame variables like screeen
    pygame.init()

    screen_size=(1500, 600)
    screen=pygame.display.set_mode(screen_size)

    pygame.display.set_caption('Show speech') 

    return screen


def paint(screen, txt, posx, posy): # function to show converted speech

    green = (0, 255, 0) 
    
    font = pygame.font.Font('freesansbold.ttf', 18) 
    screen.fill((0, 0, 0), rect=[posx, posy, (font.size(txt[0])[0]*100), 20])

    clock = pygame.time.Clock()

    text = font.render(txt, True, green) 
    
    # create a rectangular object for the text surface object
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

    posx += textRect[2]
    
    return pygame.display.get_surface(), posx, posy


def pred_show(screen, txt, posx, posy): # function to show predicted speech

    green = (0, 255, 0) 
    blue = (0, 0, 128) 

    font = pygame.font.Font('freesansbold.ttf', 18) 

    text = font.render(txt, True, green, blue) 

    # create a rectangular object for the text surface object 
    textRect = text.get_rect() 
    if((posx + textRect[2]) <= 800):
        print(str(posx+textRect[2])+ "ii")
        textRect = textRect.move(posx, posy)
    else:
        print(str(textRect[3]+ posy) + "jj")
        textRect = textRect.move(0, 300)
        #posx += textRect[2]
    pygame.display.update()
    
    # infinite loop 
    screen.blit(text, (posx, posy)) 
    pygame.display.update()
    return pygame.display.get_surface()



'''
screen = show_init()
posx = 0
posy = 0
for i in range(7):
    print(str(posx)+ "   " + str(posy))
    text = "My name is shaashwat and i am awesome" + str(i)
    posx, posy = paint(screen, text, posx, posy)'''



