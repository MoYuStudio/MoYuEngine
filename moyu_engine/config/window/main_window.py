
import arcade

import config.data.constants as C

class MainWindow(arcade.View):
    
    def __init__(self):

        super().__init__()

        self.wall_list = None
        self.player_list = None

    def setup(self):

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.scene = arcade.Scene()

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        image_source = 'tileland1.png'

        self.player_sprite = arcade.Sprite(image_source, C.tilemap['tile_size_level'])

        self.player_sprite.center_x = 100
        self.player_sprite.center_y = C.window['height']-100

        self.player_list.append(self.player_sprite)

    def on_draw(self):

        arcade.start_render()

        self.scene.draw()

        self.player_list.draw()
