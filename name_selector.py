
import pygame,sys
#from pointers import Crosshair
from buttons import Button
from pygame_functions import *

class Name_Selection():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.playing =True
        self.display_width,self.display_height = 1000,1000
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("Player name selection")
        self.background = pygame.image.load("assets/playernameselection.png")
        pygame.mouse.set_visible(True)
        #self.crosshair = Crosshair("assets/crosshair_new.png")
        #self.crosshair_group = pygame.sprite.Group()
        #self.crosshair_group.add(self.crosshair)
    def screen_loop(self):
        while self.playing:
            self.check_events()
            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            #self.crosshair_group.draw(self.screen)
            #self.crosshair_group.update()
            self.clock.tick(60)
            #Exit button
            self.exitbutton = Button(image = pygame.image.load("assets/exitbutton.png"),pos=(950,10))
            self.exitbutton.update(self.screen)
            #confirm_button
            self.confirmation_button = Button(image = pygame.image.load("assets/confirmation_playerselection.png"),pos=(744,926))
            self.confirmation_button.update(self.screen)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running,self.playing = False,False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exitbutton.check_for_input(pygame.mouse.get_pos()):
                    self.exitbutton.play_music("assets/music_and_sounds/exitbutton.wav")
                    self.playing = False
                if self.confirmation_button.check_for_input(pygame.mouse.get_pos()):
                    self.confirmation_button.play_music("assets/music_and_sounds/itemplace.wav")
                    
                print(pygame.mouse.get_pos())

            
if __name__=="__main__":
    wot_players=Name_Selection()
    wot_players.screen_loop()


