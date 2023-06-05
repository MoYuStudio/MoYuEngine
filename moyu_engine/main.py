
import pyray

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def main():
    pyray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'MoYuEngine')
    
    icon_image = pyray.load_image('moyu_engine/assets/block/1.png')
    pyray.set_window_icon(icon_image)

    while not pyray.window_should_close():

        if pyray.is_key_pressed(pyray.KEY_SPACE):
            print('space')

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)

        pyray.end_drawing()

    pyray.close_window()

if __name__ == '__main__':
    main()
