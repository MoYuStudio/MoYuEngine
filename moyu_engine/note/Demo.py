
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,500),0,32)
surface = pygame.Surface((500,500)).convert_alpha()
clock = pygame.time.Clock()

player = pygame.Rect(30,30,30,30)
pre_tile = pygame.Rect(0,0,30,30)
build_tile = pygame.Rect(0,0,30,30)


# [
# [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
# [1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0],
# [1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0],
# [1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0],
# [1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0],
# [1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0],
# [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0],
# [1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0],
# [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
# [1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0],
# ]

tile_map = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for y in range(0,25,1) ]

rect_map = []




up = False
down = False
left = False
right = False

RUN = True

speed = 3

pygame.display.set_caption('Physics Explanation')

def collision(rect,tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions
 
def move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = collision(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right
    rect.y += movement[1]
    collisions = collision(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect

while RUN:

    for y in range(len(tile_map)):
        for x in range(len(tile_map[y])):
            if tile_map[y][x] == 0:
                pass
            if tile_map[y][x] == 1:
                rect_map.append(pygame.Rect(x*30,y*30,30,30))
    
    surface.fill((0,0,0))
 
    movement = [0,0]

    if up == True:
        movement[1] -= speed
    if down == True:
        movement[1] += speed
    if left == True:
        movement[0] -= speed
    if right == True:
        movement[0] += speed

    player = move(player,movement,rect_map)
 
    pygame.draw.rect(surface,(255,255,255),player)
 
    for tile in rect_map:
        pygame.draw.rect(surface,(255,0,0),tile)

    pygame.draw.rect(surface,(255,255,0,25),pre_tile)

    screen.blit(surface,(0,0))
    
    for event in pygame.event.get():

        if event.type == QUIT:
            RUN = False
            pygame.quit()

        if event.type == MOUSEMOTION:
            mouse_motion_pos = event.pos
            pre_tile_pos = int(mouse_motion_pos[0]/30)*30,int(mouse_motion_pos[1]/30)*30
            pre_tile = pygame.Rect(pre_tile_pos[0],pre_tile_pos[1],30,30)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            build_tile_pos = int(mouse_motion_pos[0]/30)*30,int(mouse_motion_pos[1]/30)*30
            build_tile = pygame.Rect(build_tile_pos[0],build_tile_pos[1],30,30)
            tile_map[int(build_tile_pos[1]/30)][int(build_tile_pos[0]/30)] = 1

        # if event.type == pygame.MOUSEBUTTONUP:
        #     mouse_click_pos = [-1,-1]
            

        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                up = True
            if event.key == K_DOWN or event.key == K_s:
                down = True
            if event.key == K_LEFT or event.key == K_a:
                left = True
            if event.key == K_RIGHT or event.key == K_d:
                right = True
            
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_w:
                up = False
            if event.key == K_DOWN or event.key == K_s:
                down = False
            if event.key == K_LEFT or event.key == K_a:
                left = False
            if event.key == K_RIGHT or event.key == K_d:
                right = False
    
    pygame.display.update()
    clock.tick(60)