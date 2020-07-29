import pygame
import random
from pygame import surface
from pygame import rect
def main():
    #setup
    pygame.init()

    white = (255,255,255)
    black = (0,0,0)

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    colors = [red, green, blue, white]

    gameDisplay = pygame.display.set_mode((800,600))
    gameDisplay.fill(black)
    gamesurface = pygame.display.get_surface()
    pixAr = pygame.PixelArray(gameDisplay)
    


    #game
    shapes = []
    coords = []
    coords.append([random.randrange(0, 800), random.randrange(0, 600)])
    shapes.append(pygame.draw.circle(gameDisplay, random.choice(colors), coords[len(coords) - 1], 25))
    print(shapes)


    count = 0
    
    pygame.display.set_caption(str(count))


    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(shapes)): 
                    shape = shapes[i]
                    if shape.collidepoint(pygame.mouse.get_pos()):
                        count += 1
                        pygame.display.set_caption(str(count)))

                        #cover old shape
                        pygame.draw.circle(gameDisplay, black, coords[i], 25)
                        shapes.remove(shape)
                        coords.remove(coords[i])

                        #draw new shape
                        coords.append([random.randrange(0, 800), random.randrange(0, 600)])
                        shapes.append(pygame.draw.circle(gameDisplay, random.choice(colors), coords[len(coords) - 1], 25))
                        break
        if count == 10:
            break #game finishes
            

        pygame.display.update()
    
main()