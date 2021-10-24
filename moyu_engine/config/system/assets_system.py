
import os
import sys

import config.data.constants as C

class AssetsSystem:

    @ staticmethod
    def loader(folder_path = 'moyu_engine/assets'):
        def cleaner(path):
            if path.endswith('.DS_Store'):  # Mac OS
                os.remove(path)
            if path.endswith('.ini'):       # Windows
                os.remove(path)
            if path.endswith('.db'):        # Windows
                os.remove(path)
            else: 
                pass

        for root,dirs,files in os.walk(folder_path): 
            for file in files: 
                cleaner(os.path.join(root,file))
            for dir in dirs:
                C.assets[dir] = []
                path = root+'/'+dir+'/'
                file_num = len(os.listdir(path))
                tmp = os.listdir(path)
                for file_name in tmp:
                    file_num -= 1
                    if file_name.endswith('.ttf'):
                        C.assets[dir].append(os.path.join(path,dir+f'{file_num}.ttf'))
                        
                    if file_name.endswith('.png'):
                        C.assets[dir].append(os.path.join(path,dir+f'{file_num}.png'))

if __name__ == "__main__":
    pass
