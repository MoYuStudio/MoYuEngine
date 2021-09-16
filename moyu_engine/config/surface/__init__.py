
from .background import BackgroundSurface
from .map import MapSurface
from .info import InfoSurface
from .gui import MainMenuSurface, CreateNewGameSurface
from .popup import PopupSurface
from .transition import TransitionSurface

class SurfaceManager:
    def __init__(self):
        self.background = BackgroundSurface()
        self.mainmenu = MainMenuSurface(self.recall)
        self.create_newgame = CreateNewGameSurface(self.recall)

        self.stack = [self.background,self.mainmenu]
        self.recall_str = ''

    def __iter__(self):
        return iter(self.stack)
    
    def __getattr__(self, name: str):
        if name == 'R':
            return iter(self.stack[::-1])
        else:
            raise AttributeError(f"SurfaceManager can't dispose attr: {name}")

    def recall(self,s):
        self.recall_str = s
    
    def update(self):
        if self.recall_str == 'create_new_game':
            self.stack.pop()
            self.stack.append(self.create_newgame)
            self.recall_str = ''
        elif self.recall_str == 'main_menu':
            self.stack.pop()
            self.stack.append(self.mainmenu)
            self.recall_str = ''