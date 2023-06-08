
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

class Window:
    def __init__(self, title = 'MoYuEngine', width = 360, height = 180):
        self.title = title
        
        self.width = width
        self.height = height
        
        self.icon = 'moyu_engine/assets/block/1.png'
        
        self.fps_display = False
    
    def set(self):
        pyray.init_window(self.width, self.height, self.title)
        self.icon_image = pyray.load_image(self.icon)
        pyray.set_window_icon(self.icon_image)
        
        self.load()
        
        while not pyray.window_should_close():
            
            self.input()

            if pyray.is_key_pressed(pyray.KEY_ESCAPE):
                break
            
            self.logic()
            
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            
            self.render()
            
            if self.fps_display:
                fps = pyray.get_fps()
                pyray.draw_text(f"FPS: {fps}", 10, 10, 20, pyray.GREEN)
            
            pyray.end_drawing()
            
        self.clean()

        pyray.close_window()
    
    def load(self):
        pass
    
    def input(self):
        pass
    
    def logic(self):
        pass
    
    def render(self):
        pass
    
    def clean(self):
        pass
            
if __name__ == '__main__':
    win = Window()
    win.set()
