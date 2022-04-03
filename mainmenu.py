
import pygame,sys
from buttons import Button
from maingame import Game
from pygame import mixer
from creditsscreen import Credits_screen
from settingscreen import Settings_Screen
class start_menu():
    def __init__(self) -> None:
    
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("AI Tac Toe")
        self.background = pygame.image.load("assets/titlescreen.png")



        
    def maingame(self):
        while True:
            pygame.mouse.set_visible(True)
            self.playbutton = Button(image = pygame.image.load("assets/play_button.png"),pos=(733,500))
            self.playbutton.update(self.screen)
            self.settingsbutton = Button(image = pygame.image.load("assets/settings.png"),pos=(733,700))
            self.settingsbutton.update(self.screen)
            self.creditsbutton = Button(image=pygame.image.load("assets/credits.png"),pos=(733,900))
            self.creditsbutton.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.playbutton.check_for_input(pygame.mouse.get_pos()):
                            self.playbutton.play_music("assets/music_and_sounds/playbutton.wav")
                            gaem = Game()
                            gaem.game_loop()
                        if self.settingsbutton.check_for_input(pygame.mouse.get_pos()):
                            self.settingsbutton.play_music("assets/music_and_sounds/playbutton.wav")
                            settings_show = Settings_Screen()
                            settings_show.screen_loop()
                        if self.creditsbutton.check_for_input(pygame.mouse.get_pos()):
                            self.creditsbutton.play_music("assets/music_and_sounds/playbutton.wav")
                            credits_show = Credits_screen()
                            credits_show.screen_loop()

                        #print(pygame.mouse.get_pos())

            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            self.clock.tick(60)
if __name__=="__main__":

    menu=start_menu()
    menu.maingame()


    
