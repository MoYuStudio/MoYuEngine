
import arcade

window =\
{
    # window
    'size'         : [1280,720],
    'set_size'     : [320,180],
    'size_level'   : 0.5,
    'fps'          : 60,
    'title'        : 'Tinyland 弹丸之地',
    'surface_level': 1,
}

tilemap =\
{
    # tilemap
    'tilemap': [],
    'boarder': 32,
    'seed'   : 0,
    'octaves': 2,
    'freq'   : 12,

    # tile
    'tile_size'       : 64,
    'tile_size_level' : 1,
    'pretile_type'    : 0,
    'tile_type'       : 0,
    'build'           : False,
    'reward'          : False,
    'tile_choose'     : False,
    'tile_choose_info': [0,0,0],
    'tile_choose_info': [0,0,0,0,0,0],
    
    # tile time
    'time_speed': 1000,
}


class MainView(arcade.View):
    
    def __init__(self):

        super().__init__()

        self.wall_list = None
        self.player_list = None

    def setup(self):

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.scene = arcade.Scene()

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        self.player_sprite = arcade.Sprite('tileland1.png', tilemap['tile_size_level'])

        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120

        self.player_list.append(self.player_sprite)

    def on_draw(self):

        arcade.start_render()

        self.scene.draw()

        self.player_list.draw()

def main():

    screen = arcade.Window(window['size'][0], window['size'][1], window['title'])

    mainview = MainView()

    screen.show_view(mainview)

    mainview.setup()
    arcade.run()


if __name__ == "__main__":
    main()