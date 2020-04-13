
import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

gameDispaly = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CONTROL')

pygame.display.update()

gameExit = False

lead_x = 300
lead_y = 300

joysticks = []
clock = pygame.time.Clock()

for i in range (0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '", joysticks[-1].get_name(), "'")

while not gameExit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit event
            gemeExit = True
    if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                lead_y = lead_y -10
            if event.button == 2:
                lead_y = lead_y + 10
            if event.button == 3:
                lead_x = lead_x -10
            if event.button == 1:
                lead_x = lead_x + 10

    gameDispaly.fill(red)

    pygame.draw.rect(gameDispaly, white, [lead_x,lead_y,20,20])

    pygame.display.update()

pygame.quit()

quit()

