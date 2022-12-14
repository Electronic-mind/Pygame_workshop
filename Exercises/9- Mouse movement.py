import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT =300 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

#Load images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT :
            running = False

        #Move based on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

        #Drag the object only when the mouse is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    #Cover the old images
    display_surface.fill((0,0,0))

    #Blit (copy) assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()