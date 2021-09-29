
import os
import sys
import pygame
from pygame.locals import *

from operator import itemgetter 
import data.constants as C

class AssetsSystem:

    pygame.display.set_mode(C.window['size'],pygame.RESIZABLE)

    @ staticmethod
    def loader():
        def cleaner(path):
            if path.endswith('.DS_Store'):  # Mac OS
                os.remove(path)
            if path.endswith('.ini'):       # Windows
                os.remove(path)
            if path.endswith('.db'):        # Windows
                os.remove(path)
            else: 
                pass

        for root,dirs,files in os.walk('moyu_engine/assets'): 
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
                        C.assets[dir].append(pygame.font.Font(os.path.join(path,file_name),25))
                        
                    if file_name.endswith('.png'):
                        C.assets[dir].append(pygame.image.load(os.path.join(path,dir+f'{file_num}.png')))#.convert_alpha()

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    assets = {}

    def loader():
        def cleaner(path):
            if path.endswith('.DS_Store'):  # Mac OS
                os.remove(path)
            if path.endswith('.ini'):       # Windows
                os.remove(path)
            if path.endswith('.db'):        # Windows
                os.remove(path)
            else: 
                pass

        for root,dirs,files in os.walk('moyu_engine/assets'): 
            for file in files: 
                cleaner(os.path.join(root,file))
            for dir in dirs:
                assets[dir] = []
                path = root+'/'+dir+'/'
                tmp = os.listdir(path)
                file_num = len(os.listdir(path))
                # for num in range(len(os.listdir(path))):
                for file_name in tmp: 
                    file_num -= 1
                    if file_name.endswith('.ttf'):
                        # assets[dir].append(pygame.font.Font(os.path.join(path,file_name),25))
                        # print(dir)
                        # print(file_name)
                        pass
                        
                    if file_name.endswith('.png'):
                        # for num in range(len(os.listdir(path))):
                        print(dir+f'{file_num}.png')
                        # assets[dir].append(pygame.image.load(os.path.join(path,dir+f'{num}.png')))#.convert_alpha()
                        # print(dir)
                        

    loader()
    print(assets)

#     @ staticmethod
#     def input_all():
#         AssetsSystem.font()
#         #AssetsSystem.font_zh()
#         AssetsSystem.tile_tileland()
#         AssetsSystem.gui_button()
#         AssetsSystem.input_button()
#         AssetsSystem.background()

    # @ staticmethod
    # def file_cleaner(path,accept):
    #     name, ext = os.path.splitext(path)
    #     if ext.lower() in accept:
    #         pass

    # @ staticmethod
    # def cleaner(path):
    #     path = path+'/'
    #     tmp = os.listdir(path)
    #     for f in tmp: 
    #         print(f)
    #         if f.endswith('.DS_Store'):  # Mac OS
    #             os.remove(path+str(f))
    #         if f.endswith('.ini'):       # Windows
    #             os.remove(path+str(f))
    #         if f.endswith('.db'):        # Windows
    #             os.remove(path+str(f))
    #         else: 
    #             pass

    # @ staticmethod
    # def loader(assets,path):
    #     def cleaner(path):
    #         path = path+'/'
    #         tmp = os.listdir(path)
    #         for f in tmp: 
    #             print(f)
    #             if f.endswith('.DS_Store'):  # Mac OS
    #                 os.remove(path+str(f))
    #             if f.endswith('.ini'):       # Windows
    #                 os.remove(path+str(f))
    #             if f.endswith('.db'):        # Windows
    #                 os.remove(path+str(f))
    #             else: 
    #                 pass
    #     def loader(path,file,num):
    #         path = path+'/'
    #         tmp = os.listdir(path)
    #         for f in tmp: 
    #             print(f)
    #             if f.endswith('.ttf'):
    #                 file.append(pygame.font.Font(os.path.join(path,file+f'{num}.ttf'),25))
    #             if f.endswith('.png'):
    #                 file.append(pygame.image.load(os.path.join(path,file+f'{num}.png'),25))
    #             else: 
    #                 pass

    #     assets = assets.values()
    #     path = 'moyu_engine/assets'
    #     cleaner(path)
    #     folder_num = len(os.listdir(folder_path))
    #     for num in range(folder_num):
    #         loader(folder_path,folder_list,num)

        # for the_file_num in range(0,folder_num,1):
        #     file_path = folder_path+'/'+folder_list[the_file_num]
        #     cleaner(file_path)
        #     file_num = len(os.listdir())
        #     for num in range(0,file_num,1):
        #         C.assets['font'][folder_list[the_file_num]].append(pygame.font.Font(os.path.join(file_path,folder_list[the_file_num]+f'{num}.ttf'),25))



    # @ staticmethod
    # def font():
    #     folder_list = ['en','zh']
    #     folder_path = 'moyu_engine/assets/font'
    #     AssetsSystem.file_cleaner(folder_path)
    #     folder_num = len(os.listdir(folder_path))
    #     for the_file_num in range(0,folder_num,1):
    #         file_path = folder_path+'/'+folder_list[the_file_num]
    #         AssetsSystem.file_cleaner(file_path)
    #         file_num = len(os.listdir())
    #         for num in range(0,file_num,1):
    #             C.assets['font'][folder_list[the_file_num]].append(pygame.font.Font(os.path.join(file_path,folder_list[the_file_num]+f'{num}.ttf'),25))

    # @ staticmethod
    # def tile_tileland():
        
    #     path = 'moyu_engine/assets/graphics/tile/tileland'
    #     filenum = len(os.listdir(path))-1
    #     for num in range(0,filenum,1):
    #         C.assets['tile']['tileland'].append(pygame.image.load(os.path.join(path, f'tileland{num}.png')).convert_alpha())
    
    # @ staticmethod
    # def gui():
    #     folder_list = ['button','input']
    #     folder_path = 'moyu_engine/assets/graphics'
    #     AssetsSystem.file_cleaner(folder_path)
    #     folder_num = len(os.listdir(folder_path))
    #     for the_file_num in range(0,folder_num,1):
    #         file_path = folder_path+'/'+folder_list[the_file_num]
    #         AssetsSystem.file_cleaner(file_path)
    #         file_num = len(os.listdir())
    #         for num in range(0,file_num,1):
    #             C.assets['gui'][folder_list[the_file_num]].append(pygame.image.load(os.path.join(file_path,folder_list[the_file_num]+f'{num}.png')).convert_alpha())


    # @ staticmethod
    # def gui_button():
        
    #     path = 'moyu_engine/assets/graphics/gui/button'
    #     filenum = len(os.listdir(path))
    #     for num in range(0,filenum,1):
    #         C.assets['gui']['button'].append(pygame.image.load(os.path.join(path, f'button{num}.png')).convert_alpha())

    # @ staticmethod
    # def input_button():
        
    #     path = 'moyu_engine/assets/graphics/gui/input'
    #     filenum = len(os.listdir(path))
    #     for num in range(0,filenum,1):
    #         C.assets['gui']['input'].append(pygame.image.load(os.path.join(path, f'input{num}.png')).convert_alpha())

    # @ staticmethod
    # def background():
        
    #     path = 'moyu_engine/assets/graphics/background'
    #     filenum = len(os.listdir(path))
    #     for num in range(0,filenum,1):
    #         C.assets['background'].append(pygame.image.load(os.path.join(path, f'background{num}.png')).convert_alpha())




    # assets = AssetsSystem()
    # assets.tileland()
    # print(C.assets)
    # assets =\
    # {
    #     'font':
    #     {
    #         'en':[],
    #         'zh':[],
    #     },
    #     'graphics':{
    #         'tile':
    #         {
    #             'tileland'    : [],
    #             'tilebuilding': [],
    #         },
    #         'gui':
    #         {
    #             'button': [],
    #             'input' : [],
    #         },
    #         'background': []
    #     },
        
    # }


    # def loader(path,file,num):
    #     path = path+'/'
    #     tmp = os.listdir(path)
    #     for f in tmp: 
    #         print(f)
    #         if f.endswith('.ttf'):
    #             file.append(pygame.font.Font(os.path.join(path,file+f'{num}.ttf'),25))
    #         if f.endswith('.png'):
    #             file.append(pygame.image.load(os.path.join(path,file+f'{num}.png'),25))
    #         else: 
    #             pass

    # folder_list = {}
    # for folder in assets.items():
    #     if isinstance(folder, list) :
    #         for folder in assets.iter():
    #             print('1')
    #             print(folder)
    #     if isinstance(folder, tuple) :
    #         for folder in assets.items():
    #             print('2')
    #             print(folder)
    #             for folder in assets.values():
    #                 print('2-1')
    #                 print(folder)
    #         if isinstance(folder, dict) :
    #             for folder in folder.items():
    #                 # print('3')
    #                 # print(folder)
    #                 for folder in assets.values():
    #                     print('3-1')
    #                     print(folder)
    #     else:
    #         pass

    # the best
    # for root,dirs,files in os.walk('moyu_engine/assets'): 
    #     for file in files: 
    #         cleaner(os.path.join(root,file))



            
            # filenum = len(os.listdir(path))
            # for num in range(0,filenum,1):
            #     assets[dir].append(dir+str(num))

    #print(assets)

            # print(dir)
            #print(root+'/'+dir)
            # print(files)
            # a = os.listdir(root+'/'+dir)
            # print(a)
            # if a.endswith('.ttf'):
            #     assets[dir].append('ttf')
            #     print(assets)
                

            # for num in range(len(root+'/'+dir)):
            #     if (root+'/'+dir).endswith('.ttf'):
            #         print(1)

            # path = root+'/'+dir
            # filenum = len(os.listdir(path))
            # for num in range(0,filenum,1):
            #     C.assets['background'].append(pygame.image.load(os.path.join(path, f'background{num}.png')).convert_alpha())

                



            # folder_num = len(file1)

            # for num in range(0,folder_num,1):
            #     print(file1[num])
                # if root.endswith(dir[num]):
                #     print(num)

            #print(dir)
            #print(os.path.join(root,dir))

            # if root.endswith('font'):
            #     print(os.path.join(root,dir))
            #     print(dir)
            # if root.endswith('graphics'):
            #     print(os.path.join(root,dir))
            #     print(dir)
                
                
                    #assets['font']['zh'][num].append(pygame.font.Font(os.path.join(root,file)),25)
            # print(os.path.join(root,file))
            # cleaner(os.path.join(root,file))
            # sorted(os.path.join(root,file), key='.png', reverse=False)  
            # print(os.path.join(root,file))
            # 
    # sorted(file1, key=itemgetter(3), reverse=False) 
    # print(file1)        
#print(assets)
