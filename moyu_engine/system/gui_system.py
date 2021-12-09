
import sys 
sys.path.append('moyu_engine') 

import components as c

class GuiSystem():
    def __init__(self):
        self.window = c.window.Window()
        self.surface = c.surface.Surface()
        self.ui = c.ui.Ui()
        self.event = c.event.Event()

        self.config = {
                        'window':self.window.config,
                        'surface':self.surface.config,
                        'ui':self.ui.config,
                        'event':self.event.config,
                        }

    def set(self,suface_blit,event_blit):
        
        while True:
            suface_blit()
            self.window.set()
            self.surface.config['blit_window'] = self.window.screen
            self.surface.blit()
            self.event.blit()
            
            self.event.set()
            event_blit()

if __name__=="__main__":
    gui = GuiSystem()
    gui.set()