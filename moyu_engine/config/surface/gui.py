
import sys

import pygame
import pygame.locals as pglocals
import pygame.mouse

import config

import system.setting as S
import system.assets as A

class GuiSurface:
    def __init__(self,alpha_color=(0,0,0,0)):
        self.surface_size = S.WINDOW_SIZE
        self.surface = pygame.Surface(S.WINDOW_SIZE,flags=pglocals.SRCALPHA).convert_alpha()
        self.surface.fill(alpha_color)
        # initial button text here
        self.button_text = (
            A.font1.render('新游戏', True, (255, 255, 255)),
            A.font1.render('继续', True, (255, 255, 255)),
            A.font1.render('设置', True, (255, 255, 255)),
            A.font1.render('退出', True, (255, 255, 255)),
            A.font1.render('关于', True, (255, 255, 255))
        )
        button_num = len(self.button_text)
        self.button_text_pos = tuple((S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*(button_num-i) - 10*(button_num-i)) for i in range(button_num))
        # initial button texture here
        self.button_texture = (A.button001_unclickFin, A.button001_preclickFin, A.button001_clickedFin)
        self.button_texture_status = [0] * button_num
        self.button_texture_pos = tuple((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*(button_num-i) - 10*(button_num-i)) for i in range(button_num))
        self.button_texture_rect = tuple(pygame.Rect(pos[0],pos[1],64*3,16*3) for pos in self.button_texture_pos)
        # initial button logic here
        def new_game():
            # start new game here
            pass
        def continue_game():
            # continue game here
            pass
        def setting():
            # open setting ui here
            pass
        def quit():
            # quit game here
            pygame.quit()
            sys.exit()
        def about():
            # show about info here
            pass
        self.button_logic = (new_game,continue_game,setting,quit,about)
        # flag
        self.update_flag = True
    
    def update(self,interval):
        if self.update_flag:
            # clear color
            self.surface.fill((0,0,0,0))
            # blit button texture here
            for i,bs in enumerate(self.button_texture_status):
                self.surface.blit(self.button_texture[bs], self.button_text_pos[i])
            # blit button text here
            for i,text in enumerate(self.button_text):
                self.surface.blit(text, self.button_text_pos[i])
            # update finished
            self.update_flag = False

            # self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
            # self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
            # self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
            # self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
            # self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
            # self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
            # self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
            # self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
            # self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
            # self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))
        return self.surface

    def accept(self,evt):
        # button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
        # button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
        # button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
        # button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
        # button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

        # if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
        #     S.button_sound.play()

        #     MENUmain = False
        #     GAMEmain = True

        # if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
        #     S.button_sound.play()

        #     MENUmain = False
        #     GAMEmain = True

        # if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
        #     S.button_sound.play()

        # if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
        #     S.button_sound.play()

        #     pygame.quit()
        #     sys.exit()

        # if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
        #     S.button_sound.play()
        #     return False
        
        # check mouse_motion and mouse_button_down event
        if evt.type == pglocals.MOUSEMOTION or evt.type == pglocals.MOUSEBUTTONDOWN:
            for i,br in enumerate(self.button_texture_rect):
                if br.collidepoint(evt.pos):
                    # S.button_sound.play()
                    if mlb:=pygame.mouse.get_pressed()[0]:      # mouse_left_button
                        if self.button_texture_status[i] != 2:  # pressed
                            self.button_texture_status[i] = 2
                            self.update_flag = True
                    else:
                        if self.button_texture_status[i] != 1:  # focused
                            self.button_texture_status[i] = 1
                            self.update_flag = True
                    break
                else:
                    if self.button_texture_status[i] != 0:      # unfocused
                        self.button_texture_status[i] = 0
                        self.update_flag = True
            return True             # abort event distribution
        # check mouse_button_up event
        elif evt.type == pglocals.MOUSEBUTTONUP:
            for i,br in enumerate(self.button_texture_rect):
                if br.collidepoint(evt.pos):
                    if self.button_texture_status[i] != 1:      # focused
                        self.button_texture_status[i] = 1
                        self.update_flag = True
                    self.button_logic[i]()                      # run logic code
                    break
                else:
                    if self.button_texture_status[i] != 0:      # unfocused
                        self.button_texture_status[i] = 0
                        self.update_flag = True
            return True             # abort event distribution
        else:
            return False            # this event should be disposed by other surface


# def blit():
#     suface()

# def suface():

#     self.surface.fill((0,0,0,0))
#     self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
#     button_text = A.font1.render('新游戏', True, (255, 255, 255))
#     self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
#     self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
#     button_text = A.font1.render('继续', True, (255, 255, 255))
#     self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
#     self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
#     button_text = A.font1.render('设置', True, (255, 255, 255))
#     self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
#     self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
#     button_text = A.font1.render('退出', True, (255, 255, 255))
#     self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
#     self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
#     button_text = A.font1.render('关于', True, (255, 255, 255))
#     self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

#     S.SCREEN.blit(self.surface, (0, 0))

# def event():

#     button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
#     button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
#     button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
#     button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
#     button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

#     if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
#         S.button_sound.play()

#         moyu_engine.config.components.tilemap_manager.tilemap_builder()

#         MENUmain = False
#         GAMEmain = True

#     if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
#         S.button_sound.play()

#         moyu_engine.config.components.read_data.read_tilemap()

#         MENUmain = False
#         GAMEmain = True

#     if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
#         S.button_sound.play()

#     if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
#         S.button_sound.play()

#         pygame.quit()
#         sys.exit()

#     if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
#         S.button_sound.play()
        button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
        button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
        button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
        button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
        button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

        if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
            S.button_sound.play()

            MENUmain = False
            GAMEmain = True

        if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
            S.button_sound.play()

            MENUmain = False
            GAMEmain = True

        if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
            S.button_sound.play()

        if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
            S.button_sound.play()

            pygame.quit()
            sys.exit()

        if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
            S.button_sound.play()
            return False

'''

def blit():
    suface()

def suface():

    self.surface.fill((0,0,0,0))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5))
    button_text = A.font1.render('新游戏', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*5 - 10*5))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4))
    button_text = A.font1.render('继续', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*4 - 10*4))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3))
    button_text = A.font1.render('设置', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*3 - 10*3))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2))
    button_text = A.font1.render('退出', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*2 - 10*2))
    self.surface.blit(A.button001_unclickFin, (S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1))
    button_text = A.font1.render('关于', True, (255, 255, 255))
    self.surface.blit(button_text,(S.WINDOW_SIZE[0]-64*2.5*1, S.WINDOW_SIZE[1]-16*2.87*1 - 10*1))

    S.SCREEN.blit(self.surface, (0, 0))

def event():

    button01_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*5 - 10*5,64*3,16*3),width=0)
    button02_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*4 - 10*4,64*3,16*3),width=0)
    button03_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*3 - 10*3,64*3,16*3),width=0)
    button04_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*2 - 10*2,64*3,16*3),width=0)
    button05_RECT = pygame.Rect((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*1 - 10*1,64*3,16*3),width=0)

    if pygame.Rect.collidepoint(button01_RECT,S.MOUSE_POS):
        S.button_sound.play()

        moyu_engine.config.components.tilemap_manager.tilemap_builder()

        MENUmain = False
        GAMEmain = True

    if pygame.Rect.collidepoint(button02_RECT,S.MOUSE_POS):
        S.button_sound.play()

        moyu_engine.config.components.read_data.read_tilemap()

        MENUmain = False
        GAMEmain = True

    if pygame.Rect.collidepoint(button03_RECT,S.MOUSE_POS):
        S.button_sound.play()

    if pygame.Rect.collidepoint(button04_RECT,S.MOUSE_POS):
        S.button_sound.play()

        pygame.quit()
        sys.exit()

    if pygame.Rect.collidepoint(button05_RECT,S.MOUSE_POS):
        S.button_sound.play()
'''
