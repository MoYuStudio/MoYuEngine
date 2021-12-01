
import sys 
sys.path.append('moyu_engine') 

import components as c

class GuiSystem():
    def __init__(self):
        self.window = c.window.Window()
        # self.surface = c.surface.Surface()
        self.event = c.event.Event()

        self.gui_system_set = {
                                'window_set':self.window.window_set,
                                # 'surface_set':self.surface.surface_set,
                                # 'event_set':self.event.event_set,
                                }

    def set(self):
        self.window.set()
        while True:
            self.event.quit()

if __name__=="__main__":
    gui = GuiSystem()
    gui.set()