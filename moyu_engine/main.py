import pyray

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TILE_WIDTH = 128
TILE_HEIGHT = 128

VIEW_SPEED = 0.6

def main():
    pyray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'MoYuEngine')
    
    icon_image = pyray.load_image('moyu_engine/assets/block/1.png')
    pyray.set_window_icon(icon_image)
    
    image = pyray.load_image('moyu_engine/assets/block/1.png')
    texture = pyray.load_texture_from_image(image)

    view_x = 0
    view_y = 0

    while not pyray.window_should_close():

        if pyray.is_key_pressed(pyray.KEY_SPACE):
            print('space')

        if pyray.is_key_down(pyray.KEY_W):
            view_y -= VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_S):
            view_y += VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_A):
            view_x -= VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_D):
            view_x += VIEW_SPEED

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        
        for x in range(0, 9):
            for y in range(0, 9):
                tile_x = (x - y) * TILE_WIDTH // 2 + view_x
                tile_y = (x + y) * TILE_HEIGHT // 4 + view_y
                
                source_rect = pyray.Rectangle(0, 0, image.width, image.height)
                dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)
                rotation = 0.0
                pyray.draw_texture_pro(texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        pyray.end_drawing()
        
    pyray.unload_texture(texture)
    pyray.unload_image(image)

    pyray.close_window()

if __name__ == '__main__':
    main()
