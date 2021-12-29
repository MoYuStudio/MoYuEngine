
import pygame

class Ui:
    def __init__(self):
        self.config = {
                            # button
                            'blit_window':'',
                            'button_image':'',

                            'ui_event_preview':False,

                            'motion_pos':[-1,-1],
                            'click_pos':[-1,-1],

                            'display_pos':[0,0],
                            'button_area':[64,64],

                        }
        
    def button_set(self):
        self.button_ruct = pygame.Rect((self.config['display_pos'][0],self.config['display_pos'][1],self.config['button_area'][0],self.config['button_area'][1]),width=0)

    def button_blit(self):

        if self.config['ui_event_preview'] == True:
            pygame.draw.rect(self.config['blit_window'],(255,55,55,50),self.button_ruct,3)
        if self.config['ui_event_preview'] == False:
            pass

        self.config['blit_window'].blit(self.config['button_image'],self.button_ruct)

        # button
        if pygame.Rect.collidepoint(self.button_ruct,self.config['click_pos']):
            print('button_click')
        if pygame.Rect.collidepoint(self.button_ruct,self.config['motion_pos']):
            print('button_motion')

if __name__ == '__main__':
    pass
