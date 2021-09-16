
import sys

import pygame
import pygame.locals as pglocals
import pygame.mouse
import pygame.draw

import config

import system.setting as S
import system.assets as A

class MainMenuSurface:
    def __init__(self,recall,alpha_color=(0,0,0,0)):
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
            recall('create_new_game')
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
        return self.surface

    def accept(self,evt):
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
                    if self.button_texture_status[i] != 0:      # unfocused
                        self.button_texture_status[i] = 0
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


class CreateNewGameSurface:
    def __init__(self,recall):
        self.surface_size = S.WINDOW_SIZE
        self.surface = pygame.Surface(S.WINDOW_SIZE,flags=pglocals.SRCALPHA)
        self.surface.fill((0,0,0,0))
        # initial button texture here
        # self.button_texture = (A.button001_unclickFin, A.button001_preclickFin, A.button001_clickedFin)
        # self.button_texture_status = [0] * button_num
        # self.button_texture_pos = tuple((S.WINDOW_SIZE[0]-64*3*1 - 20, S.WINDOW_SIZE[1]-16*3*(button_num-i) - 10*(button_num-i)) for i in range(button_num))
        # self.button_texture_rect = tuple(pygame.Rect(pos[0],pos[1],64*3,16*3) for pos in self.button_texture_pos)

        # initial input rect
        w, h = S.WINDOW_SIZE
        iw, ih = 400, 50
        self.input_rect = pygame.Rect((w-iw)//2,(h-ih)//2,iw,ih)
        self.input_rect_active = False
        self.input_text = ''

        # initial button text here
        self.button_text = (
            A.font1.render('返回主界面', True, (255, 255, 255)),
            A.font1.render('开始新游戏', True, (255, 255, 255)),
        )
        button_num = len(self.button_text)
        self.button_text_pos = (self.input_rect.bottomleft, (self.input_rect.left+iw//2,self.input_rect.bottom))
        self.button_rect = tuple(pygame.Rect(p,t.get_size()) for p,t in zip(self.button_text_pos,self.button_text))

        def return_mainmenu():
            recall('main_menu')
            pass
        def new_game():
            pass
        self.button_logic = (return_mainmenu, new_game)

        self.update_flag = True
    
    def update(self,interval):
        if self.update_flag:
            if self.input_rect_active:
                pygame.draw.rect(self.surface, (0,0,0,64), self.input_rect)
            else:
                pygame.draw.rect(self.surface, (0,0,0,32), self.input_rect)
            
            for t,p in zip(self.button_text,self.button_text_pos):
                self.surface.blit(t,p)

            if self.input_text:
                it = A.font1.render(self.input_text, True, (255,255,255))
                self.surface.blit(it,self.input_rect)

            self.update_flag = False
        
        return self.surface

    def accept(self,evt):
        # check mouse_button_up event
        if evt.type == pglocals.MOUSEBUTTONUP:
            for i,br in enumerate(self.button_rect):
                if br.collidepoint(evt.pos):
                    self.button_logic[i]()
                    return True
        elif evt.type == pglocals.MOUSEBUTTONDOWN:
            self.input_rect_active = self.input_rect.collidepoint(evt.pos)
            self.update_flag = True
            return True
        elif evt.type == pglocals.KEYDOWN:
            if self.input_rect_active:
                if evt.key == pglocals.K_RETURN:
                    print(self.input_text)
                    self.input_text = ''
                elif evt.key == pglocals.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += evt.unicode
                self.update_flag = True
            return True
        return False
