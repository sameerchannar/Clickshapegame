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



    count = 0
    interval = 800
    
    pygame.display.set_caption("score: " + str(count) + "        interval: " + str(interval) + "         shapes: " + str(len(shapes)))
   

    shapelimit = 10

    prevTick = 0

    interval = 60
    clock = pygame.time.Clock()
    frames = 0


    while True:
        clock.tick(60)
        frames += 1
        

        if len(shapes) >= shapelimit:#if game is over
            pygame.display.set_caption("GAME OVER      score: " + str(count) + "        interval: " + str(interval) + "         shapes: " + str(len(shapes)))
        else: #if game is not over
            if frames % interval == 0: #interval is reached
                
                
                #draw new shape
                coords.append([random.randrange(0, 800), random.randrange(0, 600)])
                shapes.append(pygame.draw.circle(gameDisplay, random.choice(colors), coords[len(coords) - 1], 25))
                pygame.display.set_caption("score: " + str(count) + "        interval: " + str(interval) + "         shapes: " + str(len(shapes)))

        #if game is over or ongoing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and len(shapes) < shapelimit:
                for i in range(len(shapes)): 
                    shape = shapes[i]
                    if shape.collidepoint(pygame.mouse.get_pos()):
                        count += 1
                        pygame.display.set_caption("score: " + str(count) + "        interval: " + str(interval) + "         shapes: " + str(len(shapes)))
                        

                        #mask old shape with black shape
                        pygame.draw.circle(gameDisplay, black, coords[i], 25)
                        shapes.remove(shape)
                        coords.remove(coords[i])

                        
                        break
    
        if frames % 60 == 0:
            if interval > 18:
                interval -= 1

        pygame.display.update()
    
main()