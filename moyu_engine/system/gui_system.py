
import sys 
sys.path.append('moyu_engine') 

import components as c

class GuiSystem():
    def __init__(self):
        self.window = c.window.Window()
        # self.surface = c.surface.Surface()
        self.event = c.event.Event()

        self.gui_system_data = {
                                'window_data':self.window.window_data,
                                # 'surface_data':self.surface.surface_data,
                                # 'event_data':self.event.event_data,
                                }

    def set(self):
        self.window.set()
        while True:
            self.event.quit()

if __name__=="__main__":
    gui = GuiSystem()
    gui.set()