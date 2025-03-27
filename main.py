import pygame


print('Start Setup')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))

print('End Setup')

print('Loop Setup')
while True:
    # check all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close the window
            quit() # end pygame

