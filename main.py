import pygame
import math
import sys
#from pygame.locals import *


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


GREY = (64, 64, 64)
RED = (128, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (128, 128, 0)
BLACK = (0, 0, 0)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Python Graphics')

#    font = pygame.font.Font('Roboto-Regular.ttf', 24)
    getTicksLastFrame = 0

    running = True
    while running:
        for event in pygame.event.get():
            # Handle quitting
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
            if event.type == pygame.QUIT:
                running = False
                break

        # deltaTime in seconds.
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t

        # Rendering Section

        ## Clear the screen
#        screen.fill((0, 0, 0))

        # The below draws a simple rectangle, passing in the screen as a handle, the colour, then xpos, ypos, width, height
#        pygame.draw.rect(screen, RED, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50, 50))

        ## This draws something a bit more fancy
        ## Show how to play with trig and time
        col = (255*abs(math.sin(t/100)), 255*abs(math.cos(t/100)), 255*abs(math.sin(t/100)))
        dist = 200 * math.sin(t/5000)
        pygame.draw.circle(screen, col, (int(SCREEN_WIDTH/2 + (math.cos(t/1000.0)*dist)), int(SCREEN_HEIGHT/2 + (math.sin(t/1000.0) * dist))), 5)

        # Finish the render loop by flipping the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()
