
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

import pyray

class TexturesLoader:
    def __init__(self, folder_path = 'moyu_engine/assets/block', file_type = 'png', file_num = 256):
        self.folder_path = folder_path
        self.file_type = file_type
        self.file_num = file_num
        
        self.images = []
        self.textures = []
        
    def load(self):
        
        for file_id in range(self.file_num):
            try:
                filename = self.folder_path + '/' + str(file_id) + '.' + self.file_type
                image = pyray.load_image(filename)
                texture = pyray.load_texture_from_image(image)
                self.images.append(image)
                self.textures.append(texture)
                
            except:
                self.images.append(None)
                self.textures.append(None)
        
        return self.images, self.textures
    
    def unload(self):
        for texture in self.textures:
            pyray.unload_texture(texture)

        for image in self.images:
            pyray.unload_image(image)
            
if __name__ == '__main__':
    pass