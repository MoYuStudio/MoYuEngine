
import moyu_engine.config.constants as C
import moyu_engine.config.graphics as G
import moyu_engine.config.sound as S

def button_event_MOUSEBUTTONDOWN(button_width,button_height,button_x_pos,button_y_pos,mouse_x_pos,mouse_y_pos,button_name = 'button',button_type = 'button',button_type_data_1 = '0',button_type_data_2 = '0'):

    button_x = str(button_name) + '_x'
    button_y = str(button_name) + '_y'
    button_w = str(button_name) + '_w'
    button_h = str(button_name) + '_h'

    button_x, button_y = button_x_pos, button_y_pos
    button_w, button_h = button_width, button_height
                
    if button_x <= mouse_x_pos <= button_x + button_w and button_y <= mouse_y_pos <= button_y + button_h:
        print(str(button_name) + ' be clicked')

        if button_type == 'button':
            # data 1 = home_page
            if button_type_data_1 == 1:
                S.button_sound.play()

    return button_type_data_1,button_type_data_2

def button_hover(button_assets):
    pass

def button_gui():
    pass