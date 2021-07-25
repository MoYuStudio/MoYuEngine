import pygame

def test():
    pygame.init()
    pygame.mixer.init()

    # === ManinWindow 主视窗 ===

    MainWindow = pygame.display.set_mode((800, 500))

    pygame.display.set_caption('TinyLand 弹丸之地', 'SUGT06a3')

    icon = pygame.image.load('assets/image/testbuilding.png').convert_alpha()
    pygame.display.set_icon(icon)

    pygame.display.flip()