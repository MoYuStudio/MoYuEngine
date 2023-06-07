
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import random

import pyray
import noise

import moyu_engine

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

RENDER_WIDTH = 640
RENDER_HEIGHT = 360

TILE_WIDTH = 16
TILE_HEIGHT = 16

TILE_MAP_SIZE = 32

VIEW_SPEED = 0.06 * TILE_MAP_SIZE

ZOOM_SPEED = 0.006
MIN_ZOOM = 3
MAX_ZOOM = 9

ANIMATION_FRAME_INTERVAL = 0.2

textures_loader = moyu_engine.TexturesLoader(folder_path = 'moyu_engine/assets/block/', file_type = 'png', file_num = 256)

noise_map = moyu_engine.NoiseMap(size = 32)
noise_map = noise_map.berlin_noise()

def main():
    pyray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'MoYuEngine')
    
    tile_images, tile_textures = textures_loader.load()
    
    pyray.set_window_icon(tile_images[1])
    
    zoom_level = 3.0

    tile_map_width = TILE_MAP_SIZE * TILE_WIDTH
    tile_map_height = TILE_MAP_SIZE * TILE_HEIGHT

    view_x = (WINDOW_WIDTH - tile_map_width) // 2
    view_y = (WINDOW_HEIGHT - tile_map_height) // 2

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
        mouse_tile_x = (mouse_pos.x - view_x) // TILE_WIDTH
        mouse_tile_y = (mouse_pos.y - view_y) // TILE_HEIGHT

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        
        pyray.begin_mode_2d(pyray.Camera2D(
            pyray.Vector2(view_x, view_y),
            pyray.Vector2(RENDER_WIDTH / 2, RENDER_HEIGHT / 2),  # Center the camera on the render texture
            0.0,
            zoom_level
        ))

        for x in range(0, TILE_MAP_SIZE):
            for y in range(0, TILE_MAP_SIZE):
                tile_x = (x - y) * TILE_WIDTH // 2
                tile_y = (x + y) * TILE_HEIGHT // 4

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
                        dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)
                        rotation = 0.0

                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

                if x == mouse_tile_x and y == mouse_tile_y:
                    source_rect = pyray.Rectangle(0, 0, tile_images[255].width, tile_images[255].height)
                    dest_rect = pyray.Rectangle(tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)
                    rotation = 0.0

                    pyray.draw_texture_pro(tile_textures[255], source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        pyray.end_mode_2d()

        fps = pyray.get_fps()
        pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.GREEN)

        pyray.end_drawing()

    textures_loader.unload()

    pyray.close_window()

if __name__ == '__main__':
    main()
