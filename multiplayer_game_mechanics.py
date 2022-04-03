
import pygame,sys
import numpy as np
import math
from pygame import mixer


from component_placer import Components

class Multiplayer():
    def __init__(self,player1,player2) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.playing =True
        self.display_width,self.display_height = 1000,1000
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("Multiplayer")
        self.x_increment=62.5
        self.y_increment=62.5
        self.box_width=250
        self.box_height=250
        self.player1=player1
        self.player2=player2
        self.whos_turn=self.player1+"'s turn:"
        

        self.occupied=[]
        self.occupied_values=[]
        #self.possible_combinations=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8)(3,6,9),(1,5,9),(3,5,7)]
        self.turn_counter=0
        self.turn="cross"
        
        self.white = (255, 255, 255)
        self.black = (0,0,0)
        
        self.val1=self.val2=self.val3=self.val4=self.val5=self.val6=self.val7=self.val8=self.val9=""
        #picture assets
        self.player1_wins_background = pygame.image.load("assets/player1wins.png")
        self.player2_wins_background = pygame.image.load("assets/player2wins.png")
        self.draw_background = pygame.image.load("assets/draw_lul.png")


        for self.rows in range(3):
            for self.columns in range(3):
                pygame.draw.rect(self.screen,(255,255,255),(self.x_increment,self.y_increment,self.box_width,self.box_height))
                self.y_increment += 312.5
            self.x_increment+=312.5
            self.y_increment=62.5
        #print(self.coordinate_points)      
    def multiplayer_game_loop(self):
        while self.playing:
            
            
            self.font = pygame.font.Font('freesansbold.ttf', 32)
            self.text = self.font.render(self.whos_turn, True, self.white, self.black)
            self.textRect = self.text.get_rect()
            self.textRect.topleft = (20,20)
            self.screen.blit(self.text, self.textRect)            
            pygame.display.update()
            self.check_events()
    def check_placement(self):
        if (62.5<=self.pos[0]<=312.5) and (62.5<=self.pos[1]<=312.5): return 1
        elif (375<=self.pos[0]<=625) and (62.5<=self.pos[1]<=312.5): return 2
        elif (687.5<=self.pos[0]<=937.5) and (62.5<=self.pos[1]<=312.5): return 3
        elif (62.5<=self.pos[0]<=312.5) and (375<=self.pos[1]<=625): return 4
        elif (375<=self.pos[0]<=625) and (375<=self.pos[1]<=625): return 5
        elif (687.5<=self.pos[0]<=937.5) and (375<=self.pos[1]<=625): return 6
        elif (62.5<=self.pos[0]<=312.5) and (687.5<=self.pos[1]<=937.5): return 7
        elif (375<=self.pos[0]<=625) and (687.5<=self.pos[1]<=937.5): return 8
        elif (687.5<=self.pos[0]<=937.5) and (687.5<=self.pos[1]<=937.5): return 9
        else:return 0
    def cross_chance(self):
        if self.blocc_check==1:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(62.5,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==2:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(375,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==3:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(687.5,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==4:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(62.5,375))
            self.cross.update(self.screen)
        elif self.blocc_check==5:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(375,375))
            self.cross.update(self.screen)
        elif self.blocc_check==6:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(687.5,375))
            self.cross.update(self.screen)
        elif self.blocc_check==7:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(62.5,687.5))
            self.cross.update(self.screen)
        elif self.blocc_check==8:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(375,687.5))
            self.cross.update(self.screen)
        elif self.blocc_check==9:
            self.cross = Components(image = pygame.image.load("assets/cross.png"),pos=(687.5,687.5))
            self.cross.update(self.screen)
        mixer.music.load("assets/music_and_sounds/itemplace.wav")
        mixer.music.play()
    def circle_chance(self):
        if self.blocc_check==1:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(62.5,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==2:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(375,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==3:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(687.5,62.5))
            self.cross.update(self.screen)
        elif self.blocc_check==4:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(62.5,375))
            self.cross.update(self.screen)
        elif self.blocc_check==5:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(375,375))
            self.cross.update(self.screen)
        elif self.blocc_check==6:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(687.5,375))
            self.cross.update(self.screen)
        elif self.blocc_check==7:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(62.5,687.5))
            self.cross.update(self.screen)
        elif self.blocc_check==8:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(375,687.5))
            self.cross.update(self.screen)
        elif self.blocc_check==9:
            self.cross = Components(image = pygame.image.load("assets/circle.png"),pos=(687.5,687.5))
            self.cross.update(self.screen)
        mixer.music.load("assets/music_and_sounds/itemplace.wav")
        mixer.music.play()
    def win_checks(self):
        
        for i in self.occupied_values:
            if i[0]==1: self.val1=i[1]
            elif i[0]==2: self.val2=i[1]
            elif i[0]==3: self.val3=i[1]
            elif i[0]==4: self.val4=i[1]
            elif i[0]==5: self.val5=i[1]
            elif i[0]==6: self.val6=i[1]
            elif i[0]==7: self.val7=i[1]
            elif i[0]==8: self.val8=i[1]
            elif i[0]==9: self.val9=i[1]
        #print(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.val9)
        if self.val1==self.val2 and self.val2==self.val3: return self.val1
        elif self.val4==self.val5 and self.val5==self.val6: return self.val4
        elif self.val7==self.val8 and self.val8==self.val9: return self.val7
        elif self.val1==self.val4 and self.val4==self.val7: return self.val1
        elif self.val2==self.val5 and self.val5==self.val8: return self.val2
        elif self.val3==self.val6 and self.val6==self.val9: return self.val3
        elif self.val1==self.val5 and self.val5==self.val9: return self.val1
        elif self.val3==self.val5 and self.val5==self.val7: return self.val3
        else:return "none"

            
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
                self.pos= pygame.mouse.get_pos()

                self.blocc_check=self.check_placement()
                if 1<=self.blocc_check<=9:
                    if self.blocc_check not in self.occupied:
                        self.turn_counter+=1
                        
                        self.occupied.append(self.blocc_check)
                        if self.turn_counter%2==0:
                            
                            
                            self.occupied_values.append((self.blocc_check,"circle"))
                            #print(self.occupied_values)
                            pygame.draw.rect(self.screen,self.black,(0,0,1000,55))
                            self.whos_turn=self.player1+"'s turn:"
                            self.circle_chance()
                            self.did_win=self.win_checks()
                            if self.did_win == "none":
                                pass
                            elif self.did_win == "cross":
                                #print("cross_wins")
                                self.whos_turn=self.player1+ " wins gg"
                                self.screen.blit(self.player1_wins_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/winscreen.wav")
                                mixer.music.play()
                            elif self.did_win == "circle":
                                #print("circle wins")
                                self.whos_turn=self.player2+ " wins gg"
                                self.screen.blit(self.player2_wins_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/winscreen.wav")
                                mixer.music.play()
                            if sorted(self.occupied)==[1,2,3,4,5,6,7,8,9]:
                                self.whos_turn="Draw"
                                self.screen.blit(self.draw_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/drawscreen.wav")
                                mixer.music.play()

                            
                        else:
                            
                            
                            self.occupied_values.append((self.blocc_check,"cross"))
                            #print(self.occupied_values)
                            pygame.draw.rect(self.screen,self.black,(0,0,1000,55))
                            self.whos_turn=self.player2+"'s turn:"
                            self.cross_chance()
                            self.did_win=self.win_checks()
                            if self.did_win == "none":
                                pass
                            elif self.did_win == "cross":
                                self.whos_turn=self.player1+ " wins gg"
                                self.screen.blit(self.player1_wins_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/winscreen.wav")
                                mixer.music.play()
                                #print("cross_wins")
                            elif self.did_win == "circle":
                                #print("circle wins")
                                self.whos_turn=self.player2+ " wins gg"
                                self.screen.blit(self.player2_wins_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/winscreen.wav")
                                mixer.music.play()
                            if sorted(self.occupied)==[1,2,3,4,5,6,7,8,9]:
                                self.whos_turn="Draw"
                                self.screen.blit(self.draw_background,(0,0))
                                mixer.music.load("assets/music_and_sounds/drawscreen.wav")
                                mixer.music.play()
                            
                    else: pass



if __name__=="__main__":
    manual_mode=Multiplayer(player1="player1",player2="player2")
    manual_mode.multiplayer_game_loop()