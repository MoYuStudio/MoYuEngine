import pygame

text = ''

pygame.init()

MainWindow = pygame.display.set_mode((640, 480))

pygame.draw.rect(MainWindow, (161, 136, 127), (200, 200, 150, 35), width=0)
pygame.display.flip()
 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == 13:
                print('enter')
            
            text_input = chr(event.key)
            print(text_input)
            text = str(text) + str(text_input)
            print(text)

            pygame.display.update()


