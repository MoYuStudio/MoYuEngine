
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

class Window:
    def __init__(self):
        self.width = 360
        self.height = 180
        
        self.title = 'MoYuEngine'
        
        self.fps_display = False
    
    def set(self):
        pyray.init_window(self.width, self.height, self.title)
        
        while not pyray.window_should_close():

            if pyray.is_key_pressed(pyray.KEY_ESCAPE):
                break
            
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            
            if self.fps_display:
                fps = pyray.get_fps()
                pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.GREEN)
            
            pyray.end_drawing()

        pyray.close_window()
            
if __name__ == '__main__':
    win = Window()
    win.set()
