
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import moyu_engine

import pyray

class Game:
    def __init__(self):
        self.window_width = 1280
        self.window_height = 720

        self.render_width = 360
        self.render_height = 180

        self.tile_width = 16
        self.tile_height = 16

        self.tile_map_size = 32

        self.view_speed = 0.06 * self.tile_map_size

        self.zoom_speed = 0.006
        self.min_zoom = 3
        self.max_zoom = 9

        self.textures_loader = moyu_engine.TexturesLoader(folder_path = 'moyu_engine/assets/block', file_type = 'png', file_num = 256)
        
        self.window = moyu_engine.Window(title = 'MoYuEngine', width = self.window_width, height = self.window_height)
        self.window.fps_display = True

        self.noise_map = moyu_engine.NoiseMap(size = 32)
        self.noise_map = self.noise_map.berlin_noise()

    def window_load(self):
    
        self.tile_images, self.tile_textures = self.textures_loader.load()
        
        self.zoom_level = 3.0

        self.tile_map_width = self.tile_map_size * self.tile_width
        self.tile_map_height = self.tile_map_size * self.tile_height

        self.view_x = (self.window_width - self.tile_map_width) // 2
        self.view_y = (self.window_height - self.tile_map_height) // 2
        
    def window_input(self):
        
        if pyray.is_key_down(pyray.KEY_W):
            self.view_y += self.view_speed
        if pyray.is_key_down(pyray.KEY_S):
            self.view_y -= self.view_speed
        if pyray.is_key_down(pyray.KEY_A):
            self.view_x += self.view_speed
        if pyray.is_key_down(pyray.KEY_D):
            self.view_x -= self.view_speed
        if pyray.is_key_down(pyray.KEY_Q):
            self.zoom_level -= self.zoom_speed
            if self.zoom_level < self.min_zoom:
                self.zoom_level = self.min_zoom
        if pyray.is_key_down(pyray.KEY_E):
            self.zoom_level += self.zoom_speed
            if self.zoom_level > self.max_zoom:
                self.zoom_level = self.max_zoom
                
    def window_logic(self):
        
        self.mouse_pos = pyray.get_mouse_position()
        self.mouse_tile_x = (self.mouse_pos.x - self.view_x) // self.tile_width
        self.mouse_tile_y = (self.mouse_pos.y - self.view_y) // self.tile_height
        
    def window_render(self):
        
        pyray.begin_mode_2d(pyray.Camera2D(
            pyray.Vector2(self.view_x, self.view_y),
            pyray.Vector2(self.render_width / 2, self.render_height / 2),
            0.0,
            self.zoom_level
        ))

        for x in range(0, self.tile_map_size):
            for y in range(0, self.tile_map_size):
                self.tile_x = (x - y) * self.tile_width // 2
                self.tile_y = (x + y) * self.tile_height // 4

                noise_value = self.noise_map[x][y]
                
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
                
                if tile_index >= 0 and tile_index < len(self.tile_textures):
                    tile_image = self.tile_images[tile_index]
                    tile_texture = self.tile_textures[tile_index]

                    if tile_image and tile_texture:
                        source_rect = pyray.Rectangle(0, 0, tile_image.width, tile_image.height)
                        dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.tile_width, self.tile_height)
                        rotation = 0.0

                        pyray.draw_texture_pro(tile_texture, source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

                if x == self.mouse_tile_x and y == self.mouse_tile_y:
                    source_rect = pyray.Rectangle(0, 0, self.tile_images[255].width, self.tile_images[255].height)
                    dest_rect = pyray.Rectangle(self.tile_x, self.tile_y, self.tile_width, self.tile_height)
                    rotation = 0.0

                    pyray.draw_texture_pro(self.tile_textures[255], source_rect, dest_rect, pyray.Vector2(0, 0), rotation, pyray.RAYWHITE)

        pyray.end_mode_2d()
        
    def window_clean(self):
        
        self.textures_loader.unload()
        
    def run(self):

        self.window.load = self.window_load
        
        self.window.input = self.window_input

        self.window.logic = self.window_logic
            
        self.window.render = self.window_render
        
        self.window.set()

if __name__ == '__main__':
    game = Game()
    
    game.run()
