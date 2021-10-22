
import arcade

class TileMap:
    def __init__(self, position_x, position_y, change_x, change_y, radius):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        image_source = 'moyu_engine/assets/graphics/tile/tileland/tileland1.png'

        tilesize = 1

        self.player_sprite = arcade.Sprite(image_source, tilesize)
        self.player_sprite1 = arcade.Sprite(image_source, tilesize)

        self.player_sprite.center_x = self.position_x
        self.player_sprite.center_y = self.position_y

        self.player_sprite1.center_x = self.position_x-(30*tilesize)
        self.player_sprite1.center_y = self.position_y-(15*tilesize)

        self.player_list.append(self.player_sprite)
        self.player_list.append(self.player_sprite1)
        self.player_list.draw()

    def update(self):
        
        self.position_y += self.change_y
        self.position_x += self.change_x