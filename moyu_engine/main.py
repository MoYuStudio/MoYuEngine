
import random

import pyray
import noise

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

TILE_WIDTH = 64
TILE_HEIGHT = 64

TILE_MAP_SIZE = 32

VIEW_SPEED = 0.06*TILE_MAP_SIZE

ZOOM_SPEED = 0.006
MIN_ZOOM = 0.6
MAX_ZOOM = 3.2

ANIMATION_FRAME_INTERVAL = 0.2

def load_tile_textures():
    tile_images = []
    tile_textures = []
    
    for i in range(1025):
        try:
            filename = f'moyu_engine/assets/block/{i}.png'
            image = pyray.load_image(filename)
            texture = pyray.load_texture_from_image(image)
            tile_images.append(image)
            tile_textures.append(texture)
            
        except:
            tile_images.append(None)
            tile_textures.append(None)
    
    return tile_images, tile_textures


def generate_noise_map(width, height):
    noise_map = [[0.0] * width for _ in range(height)]
    octaves = 2 #2
    freq = random.randint(12,16) #12
    map_seed = random.randint(100000, 999999)

    for y in range(height):
        for x in range(width):
            noise_map[y][x] = int(noise.pnoise2((x/freq)+map_seed,(y/freq)+map_seed,octaves)*100+50)

    return noise_map

def main():
    pyray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'MoYuEngine')
    
    icon_image = pyray.load_image('moyu_engine/assets/block/1.png')
    pyray.set_window_icon(icon_image)
    
    tile_images, tile_textures = load_tile_textures()

    view_x = 0
    view_y = 0
    
    zoom_level = 1.0
    
    noise_map = generate_noise_map(TILE_MAP_SIZE, TILE_MAP_SIZE)

    while not pyray.window_should_close():

        if pyray.is_key_pressed(pyray.KEY_SPACE):
            print('space')

        if pyray.is_key_down(pyray.KEY_W):
            view_y += VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_S):
            view_y -= VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_A):
            view_x += VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_D):
            view_x -= VIEW_SPEED
        if pyray.is_key_down(pyray.KEY_Q):
            zoom_level -= ZOOM_SPEED
            if zoom_level < MIN_ZOOM:
                zoom_level = MIN_ZOOM
        if pyray.is_key_down(pyray.KEY_E):
            zoom_level += ZOOM_SPEED
            if zoom_level > MAX_ZOOM:
                zoom_level = MAX_ZOOM
            
        mouse_pos = pyray.get_mouse_position()
        mouse_tile_x = (mouse_pos.x - view_x) // (TILE_WIDTH // 2)
        mouse_tile_y = (mouse_pos.y - view_y) // (TILE_HEIGHT // 4)

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        
        for x in range(0, TILE_MAP_SIZE):
            for y in range(0, TILE_MAP_SIZE):
                
                tile_x = (x - y) * TILE_WIDTH // 2 * zoom_level + view_x
                tile_y = (x + y) * TILE_HEIGHT // 4 * zoom_level + view_y

                noise_value = noise_map[x][y]
                
                if -1000 <= noise_value <= 30:
                    tile_index = 5
                elif 31 <= noise_value <= 40:
                    tile_index = 3
                elif 41 <= noise_value <= 70:
                    tile_index = 1
                elif 71 <= noise_value <= 80:
                    tile_index = 2
                elif 81 <= noise_value <= 1000:
                    tile_index = 4
                else:
                    tile_index = 0 
                
                if tile_index >= 0 and tile_index < len(tile_textures):
                    tile_image = tile_images[tile_index]
                    tile_texture = tile_textures[tile_index]

                    if tile_image and tile_texture:
                        source_rect = pyray.Rectangle(0, 0, tile_image.width, tile_image.height)
                        dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH * zoom_level, TILE_HEIGHT * zoom_level)
                        rotation = 0.0

                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

                if x == mouse_tile_x and y == mouse_tile_y:
                    source_rect = pyray.Rectangle(0, 0, tile_images[255].width, tile_images[255].height)
                    dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH * zoom_level, TILE_HEIGHT * zoom_level)
                    rotation = 0.0

                    pyray.draw_texture_pro(tile_textures[255], source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        fps = pyray.get_fps()
        pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.DARKGRAY)

        pyray.end_drawing()
        
    for texture in tile_textures:
        pyray.unload_texture(texture)

    for image in tile_images:
        pyray.unload_image(image)

    pyray.unload_image(icon_image)

    pyray.close_window()

if __name__ == '__main__':
    main()
