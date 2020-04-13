import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

RED =(255, 0, 0)
BLUE = (0,0, 255)
YELLOW = (255, 255,0)
WHITE = (255,255,255)
#BACKGROUND_COLOR = ('square.png')
IMAGE = 'square.png'

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]
lead_x = player_size

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

joysticks = []
clock = pygame.time.Clock()

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Square By Ron Dahan Controller')
img = pygame.image.load(IMAGE)
screen.blit(img, (0,0))
pygame.display.flip()
icon = pygame.image.load('startup.png')
pygame.display.set_icon(icon)
game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
    if score < 5:
        SPEED = 20
    elif score < 10:
        SPEED = 40
    elif score < 60:
        SPEED = 60
    else:
        SPEED = 10
    return SPEED

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.8:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return  score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y>= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

for i in range (0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected joystick '", joysticks[-1].get_name(), "'")
    
while not game_over:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                lead_x = lead_x -10
            elif event.button == 2:
                lead_x = lead_x + 10
                

    screen.blit(img, (0,0))

    pygame.draw.rect(screen, WHITE, [lead_x, lead_x, 50, 50])

    pygame.display.update()


            #x = player_pos[0]
            #y = player_pos[1]


            #if event.key == pygame.K_LEFT:
                #x-= player_size
            #elif event.key == pygame.K_RIGHT:
                #x+= player_size

            #player_pos = [x,y]

    screen.blit(img, (0,0))
    pygame.display.flip()

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-150, HEIGHT-40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()