
import pyray

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

TILE_WIDTH = 128
TILE_HEIGHT = 128

TILE_MAP_SIZE = 12

VIEW_SPEED = 0.1*TILE_MAP_SIZE

def main():
    pyray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'MoYuEngine')
    
    icon_image = pyray.load_image('moyu_engine/assets/block/1.png')
    pyray.set_window_icon(icon_image)
    
    image = pyray.load_image('moyu_engine/assets/block/1.png')
    texture = pyray.load_texture_from_image(image)
    
    hover_image = pyray.load_image('moyu_engine/assets/block/255.png')
    hover_texture = pyray.load_texture_from_image(hover_image)

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
            
        mouse_pos = pyray.get_mouse_position()
        mouse_tile_x = (mouse_pos.x - view_x) // (TILE_WIDTH // 2)
        mouse_tile_y = (mouse_pos.y - view_y) // (TILE_HEIGHT // 4)

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        
        for x in range(0, TILE_MAP_SIZE):
            for y in range(0, TILE_MAP_SIZE):
                tile_x = (x - y) * TILE_WIDTH // 2 + view_x
                tile_y = (x + y) * TILE_HEIGHT // 4 + view_y
                
                source_rect = pyray.Rectangle(0, 0, image.width, image.height)
                dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)
                rotation = 0.0
                
                if x == mouse_tile_x and y == mouse_tile_y:
                    pyray.draw_texture_pro(hover_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)
                else:
                    pyray.draw_texture_pro(texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        fps = pyray.get_fps()
        pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.DARKGRAY)

        pyray.end_drawing()
        
    pyray.unload_texture(texture)
    pyray.unload_image(image)

    pyray.unload_texture(hover_texture)
    pyray.unload_image(hover_image)

    pyray.close_window()

if __name__ == '__main__':
    main()
