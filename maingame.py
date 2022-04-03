import imp
import pygame,sys
from pointers import Crosshair
from buttons import Button
from player_selector_multiplayer import Name_selection
class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.playing =True
        self.display_width,self.display_height = 1000,1000
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("gamemode selector")
        self.background = pygame.image.load("assets/background.png")
        pygame.mouse.set_visible(True)
        '''self.crosshair = Crosshair("assets/crosshair_new.png")


        self.crosshair_group = pygame.sprite.Group()
        self.crosshair_group.add(self.crosshair)'''

    def game_loop(self):
        while self.playing:
            self.check_events()
            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            #self.crosshair_group.draw(self.screen)
            #self.crosshair_group.update()
            self.clock.tick(60)
            #ai button
            self.ai_gamemode = Button(image = pygame.image.load("assets/ai_selector.png"),pos=(250,500))
            self.ai_gamemode.update(self.screen)
            #multiplayer button
            self.multiplayer_gamemode = Button(image = pygame.image.load("assets/player_2.png"),pos=(750,500))
            self.multiplayer_gamemode.update(self.screen)



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
                if event.button == 1:
                    if self.multiplayer_gamemode.check_for_input(pygame.mouse.get_pos()):
                        self.multiplayer_gamemode.play_music("assets/music_and_sounds/playbutton.wav")
                        name_selector=Name_selection()
                        name_selector.update()
                        name_selector.run_multiplayer()
if __name__=="__main__":
    gmingg=Game()
    gmingg.game_loop()


