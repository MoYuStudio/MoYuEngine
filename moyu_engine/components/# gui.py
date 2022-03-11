 
import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

test_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((350, 350), (300, 20)),
                                                     start_value = 5,
                                                     value_range = [0,100],
                                                     manager = manager)

# test_slider.disable()



clock = pygame.time.Clock()
is_running = True



while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
          if event.ui_element == test_slider:
              #print('current slider value:', event.value)
              sb_v = test_slider.get_current_value( )
              print(sb_v)

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()