
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

import pyglet

import config.data.constants as C

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

image1 = pyglet.image.load('moyu_engine/assets/graphics/tile/tileland/tileland1.png')

image2 = pyglet.resource.image('moyu_engine/assets/graphics/tile/tileland/tileland1.png')

sprite = pyglet.sprite.Sprite(img=image1)

@window.event
def on_draw():
    window.clear()
    label.draw()
    image2.blit(0, 0)

pyglet.app.run()

# if __name__ == '__main__':
#     pass