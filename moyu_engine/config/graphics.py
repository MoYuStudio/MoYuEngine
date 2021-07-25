
import pygame

import constants as C

tl1 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL1.png').convert_alpha()
tl1Fin = pygame.transform.scale(tl1, (64 * C.tile_level,64 * C.tile_level))

tl6 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL6.png').convert_alpha()
tl6Fin = pygame.transform.scale(tl6, (64 * C.tile_level,64 * C.tile_level))

tl11 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL11.png').convert_alpha()
tl11Fin = pygame.transform.scale(tl11, (64 * C.tile_level,64 * C.tile_level))

tl16 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL16.png').convert_alpha()
tl16Fin = pygame.transform.scale(tl16, (64 * C.tile_level,64 * C.tile_level))

tl21 = pygame.image.load('moyu_engine/assets/graphics/tileland/TL21.png').convert_alpha()
tl21Fin = pygame.transform.scale(tl21, (64 * C.tile_level,64 * C.tile_level))

t105 = pygame.image.load('moyu_engine/assets/graphics/tile/T105.png').convert_alpha()
t105Fin = pygame.transform.scale(t105, (64 * C.tile_level,48 * C.tile_level))

pretile_choose = pygame.image.load('moyu_engine/assets/graphics/pretile/Pretilechoose.png').convert_alpha()
pretile_chooseFin = pygame.transform.scale(pretile_choose, (64 * C.tile_level,32 * C.tile_level))

pretile_green = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileGreen.png').convert_alpha()
pretile_greenFin = pygame.transform.scale(pretile_green, (64 * C.tile_level,32 * C.tile_level))

pretile_red = pygame.image.load('moyu_engine/assets/graphics/pretile/PretileRed.png').convert_alpha()
pretile_redFin = pygame.transform.scale(pretile_red, (64 * C.tile_level,32 * C.tile_level))