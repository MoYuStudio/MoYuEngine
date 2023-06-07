
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

class Window:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        
        self.title = 'MoYuEngine'
    
    def set(self):
        pyray.init_window(self.width, self.height, self.title)
        
        while not pyray.window_should_close():

            if pyray.is_key_pressed(pyray.KEY_ESCAPE):
                break
            
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            
            pyray.end_drawing()

        pyray.close_window()
            
if __name__ == '__main__':
    win = Window()
