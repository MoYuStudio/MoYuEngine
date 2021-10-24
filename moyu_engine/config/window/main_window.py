
import arcade

import config.data.constants as C

import config.components

class MainWindow(arcade.View):
    
    def __init__(self):

        super().__init__()

        self.wall_list = None
        self.player_list = None

        self.tilemap = config.components.TileMap(100, 100, 0, 0, 15)

    def setup(self):

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.scene = arcade.Scene()

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        image_source = C.assets['input'][-(22)-1]

        self.player_sprite = arcade.Sprite(image_source, 3)

        self.player_sprite.center_x = 100
        self.player_sprite.center_y = C.window['height']-100

        self.player_list.append(self.player_sprite)

    def on_draw(self):

        arcade.start_render()

        self.scene.draw()

        self.player_list.draw()

        self.tilemap.draw()

    def update(self, delta_time):
        self.tilemap.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.tilemap.change_x = -5
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.tilemap.change_x = 5
        elif key == arcade.key.UP or key == arcade.key.W:
            self.tilemap.change_y = 5
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.tilemap.change_y = -5

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.tilemap.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.tilemap.change_y = 0

