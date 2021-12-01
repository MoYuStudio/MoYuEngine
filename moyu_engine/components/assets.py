
import os
import pygame
from pygame.locals import *

class Assets:
    def __init__(self,path = 'moyu_engine/assets'):
        self.path = path
        self.assets_dictionary = {}

        pygame.display.set_mode([320,180],pygame.RESIZABLE)

    def load(self):
        def cleaner():
            if path.endswith('.DS_Store'):  # Mac OS
                os.remove(self.path)
            if path.endswith('.ini'):       # Windows
                os.remove(self.path)
            if path.endswith('.db'):        # Windows
                os.remove(self.path)
            else: 
                pass

        for root,dirs,files in os.walk(self.path): 
            for file in files: 
                cleaner(os.path.join(root,file))
            for dir in dirs:
                self.assets_dictionary[dir] = []
                path = root+'/'+dir+'/'
                file_num = len(os.listdir(path))
                tmp = os.listdir(path)
                for file_name in tmp:
                    file_num -= 1
                    if file_name.endswith('.ttf'):
                        self.assets_dictionary[dir].append(pygame.font.Font(os.path.join(path,dir+f'{file_num}.ttf'),25))
                        
                    if file_name.endswith('.png'):
                        self.assets_dictionary[dir].append(pygame.image.load(os.path.join(path,dir+f'{file_num}.png')))#.convert_alpha()
        
        return self.assets_dictionary

if __name__ == "__main__":
    pass
