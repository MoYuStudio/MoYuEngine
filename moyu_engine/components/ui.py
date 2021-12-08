
import pygame

class UI:
    def __init__(self,config={
                                'blit_window':'',
                                'button_image':'',
                                'ui_event_preview':False,
                                'event_pos':[0,0],
                                'window_x':0,
                                'window_y':0,
                                'button_width':64,
                                'button_hight':64,
                            }):
        self.config = config
        
    def button(self):
        self.button_ruct = pygame.Rect((self.config['window_x'],self.config['window_y'],self.config['button_width'],self.config['button_hight']),width=0)
    def button_blit(self):
        if self.config['ui_event_preview'] == True:
            pygame.draw.rect(self.config['blit_window'],(255,55,55,30),self.button_ruct,1)
        if self.config['ui_event_preview'] == False:
            pass

        self.config['blit_window'].blit(self.config['button_image'],self.button_ruct)

        # button
        pygame.Rect.collidepoint(self.button_ruct,self.config['event.pos'])

if __name__ == '__main__':
    pass
