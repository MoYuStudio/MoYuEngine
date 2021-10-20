
################################################################
#                    MoYu Studio © 2021                        #
################################################################
#                         Tinyland                             #
#                     SUGT06 a20 Bata                          #
################################################################
#                     Power by OpenGL                          #
#                 Pyglet & Arcade & PyMunk                     #
################################################################

import arcade

import config.data.constants as C
import config.window

def main():

    screen = arcade.Window(C.window['width'], C.window['height'], C.window['title'])

    mainview = config.window.main_window.MainWindow()

    screen.show_view(mainview)

    mainview.setup()
    arcade.run()


if __name__ == '__main__':
    main()