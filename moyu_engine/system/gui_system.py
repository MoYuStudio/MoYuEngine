
import sys 
sys.path.append('moyu_engine') 

import components as c

class GuiSystem():
    def __init__(self):
        self.window = c.window.Window()
        self.surface = c.surface.Surface()
        self.event = c.event.Event()

        self.config = {
                        'window':self.window.config,
                        'surface':self.surface.config,
                        'event':self.event.config,
                        }

    def set(self):
        self.window.set()
        self.surface.config['blit_window'] = self.window.screen
        
        while True:
            self.surface.blit()
            self.event.set()

if __name__=="__main__":
    gui = GuiSystem()
    gui.set()