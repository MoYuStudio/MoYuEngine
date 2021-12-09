
import os
import pygame
from pygame.locals import *

class Assets:
    def __init__(self):
        self.config = {
                            'file_type':'png',
                            'path':'tinyland/assets/graphics/tile',
                            'sheet_dictionary':[],
                            'data_dictionary':{},
                        }
        self.assets_dictionary = {}

        self.os_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

        pygame.display.set_mode([320,180],pygame.RESIZABLE)

    def set(self):
        for sheet_num in range(len(self.config['sheet_dictionary'])):
            for data_num in range(len(self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]])):
                if self.config['file_type'] == 'png':
                    self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]][data_num]['assets'] = pygame.image.load(self.os_path +'\\'+ self.config['path']+'\\'+str(self.config['sheet_dictionary'][sheet_num])+'\\'+str(self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]][data_num]['name'])+'.png')#.convert_alpha()

        return self.config

    # def load(self):
    #     def cleaner():
    #         if path.endswith('.DS_Store'):  # Mac OS
    #             os.remove(self.path)
    #         if path.endswith('.ini'):       # Windows
    #             os.remove(self.path)
    #         if path.endswith('.db'):        # Windows
    #             os.remove(self.path)
    #         else: 
    #             pass

    #     for root,dirs,files in os.walk(self.path): 
    #         for file in files: 
    #             cleaner(os.path.join(root,file))
    #         for dir in dirs:
    #             self.assets_dictionary[dir] = []
    #             path = root+'/'+dir+'/'
    #             file_num = len(os.listdir(path))
    #             tmp = os.listdir(path)
    #             for file_name in tmp:
    #                 file_num -= 1
    #                 if file_name.endswith('.ttf'):
    #                     self.assets_dictionary[dir].append(pygame.font.Font(os.path.join(path,dir+f'{file_num}.ttf'),25))
                        
    #                 if file_name.endswith('.png'):
    #                     self.assets_dictionary[dir].append(pygame.image.load(os.path.join(path,dir+f'{file_num}.png')))#.convert_alpha()
        
    #     return self.assets_dictionary

if __name__ == "__main__":
    a =Assets()
    a.set
    print(a.config['data_dictionary'])
