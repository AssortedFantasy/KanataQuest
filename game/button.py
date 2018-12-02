import pygame
class Button:
    def __init__(self, x, y, width, height, game_state, button_colour = (255,255,255), border_colour=(0,0,0), text="") :
        self.button_colour = button_colour
        self.border_colour = border_colour
        self.text = text
        self.font = pygame.font("Arial")
        text_width =  self.pygame.font.Font.size(self.font, self.text)
        if text_width > width:
            self.button = pygame.rect(x,y,text_width,height)
        else:
            self.button = pygame.rect(x,y,width,height)

    def draw_button(self):
