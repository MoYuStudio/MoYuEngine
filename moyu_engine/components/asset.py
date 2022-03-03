
import os
import pygame
from pygame.locals import *

class Assets:
    def __init__(self):
        
        self.file_type = 'png'
        self.path = 'tinyland/assets/graphics/tile'
        self.sheet_dictionary = []
        self.data_dictionary = {}

        self.assets_dictionary = {}

        self.os_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

        pygame.display.set_mode([320,180],pygame.RESIZABLE)

    def set(self):
        for sheet_num in range(len(self.config['sheet_dictionary'])):
            for data_num in range(len(self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]])):
                if self.config['file_type'] == 'png':
                    self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]][data_num]['assets'] = pygame.image.load(self.os_path +'\\'+ self.config['path']+'\\'+str(self.config['sheet_dictionary'][sheet_num])+'\\'+str(self.config['data_dictionary'][self.config['sheet_dictionary'][sheet_num]][data_num]['name'])+'.png')#.convert_alpha()

        return self.config