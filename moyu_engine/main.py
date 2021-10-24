
################################################################
#                     MoYu Studio © 2021                       #
################################################################
#                          Tinyland                            #
#                      SUGT06 a20 Bata                         #
################################################################
#                         MoYu Engine                          #
#                       Powed by OpenGL                        #
#                           Pyglet                             #
################################################################

import sys
import pyglet
# from pyglet.image.codecs.png import PNGImageDecoder

# import config.data.constants as C

window = pyglet.window.Window()
# , decoder=PNGImageDecoder()
image = pyglet.image.load('moyu_engine/assets/graphics/tile/tileland/tileland1.png')
sprite = pyglet.sprite.Sprite(image, 10, 10)

@window.event
def on_draw():
    window.clear()
    sprite.draw()
    

pyglet.app.run()

# if __name__ == '__main__':
#     pass