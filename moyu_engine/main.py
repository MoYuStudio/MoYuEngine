
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

import config.system
import config.data.constants as C 

window = pyglet.window.Window(
                                width     = C.window['width'],
                                height    = C.window['height'],
                                caption   = C.window['caption'],
                                resizable = C.window['resizable'],
                                vsync     = C.window['vsync'],
                            )

window.set_icon(pyglet.image.load('moyu_engine/assets/graphics/tile/tileland/tileland1.png'))


image = pyglet.image.load('moyu_engine/assets/graphics/tile/tileland/tileland1.png')

batch = pyglet.graphics.Batch()
# y*(tile_size/2)-x*(tile_size/2),y*(tile_size/4)+x*(tile_size/4)

sprite = {}
tile_size = 64
boarder = 32

fps_display = pyglet.window.FPSDisplay(window)

def foo(value):
    print('loop')

@window.event
def on_draw():

    config.system.MoveSystem.move()

    for x in range(boarder):
        sprite[x] = {}
        for y in range(boarder):
            sprite[x][y] = pyglet.sprite.Sprite(img=image,x=(y*(tile_size/2)-x*(tile_size/2))+C.window['move_x'],y=C.window['height']-(y*(tile_size/4)+x*(tile_size/4))+C.window['move_y'], batch=batch)

    window.clear()
    batch.draw()
    fps_display.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W or symbol == pyglet.window.key.UP:
        C.window['move_switch']['up'] = True
    if symbol == pyglet.window.key.A or symbol == pyglet.window.key.LEFT:
        C.window['move_switch']['left'] = True
    if symbol == pyglet.window.key.S or symbol == pyglet.window.key.DOWN:
        C.window['move_switch']['down'] = True
    if symbol == pyglet.window.key.D or symbol == pyglet.window.key.RIGHT:
        C.window['move_switch']['right'] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.W or symbol == pyglet.window.key.UP:
        C.window['move_switch']['up'] = False
    if symbol == pyglet.window.key.A or symbol == pyglet.window.key.LEFT:
        C.window['move_switch']['left'] = False
    if symbol == pyglet.window.key.S or symbol == pyglet.window.key.DOWN:
        C.window['move_switch']['down'] = False
    if symbol == pyglet.window.key.D or symbol == pyglet.window.key.RIGHT:
        C.window['move_switch']['right'] = False
    
pyglet.clock.schedule_interval(foo, 1/120)
pyglet.app.run()

# if __name__ == '__main__':
#     pass