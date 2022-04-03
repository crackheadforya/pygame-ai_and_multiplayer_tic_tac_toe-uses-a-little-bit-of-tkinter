import tkinter as tk
from multiplayer_game_mechanics import Multiplayer

from buttons import Button
class Name_selection():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("1000x1000")
        self.window.title("Player Selector")
        self.background=tk.PhotoImage(file="assets/playernameselection.png")
        self.confirmation_button= tk.PhotoImage(file="assets/confirmation_playerselection.png")
        self.label1 = tk.Label( self.window, image = self.background)
        self.label1.place(x = 0,y = 0)
        self.player1_entry=tk.Entry(self.window,width=20,font=("Helvetica",30))
        self.player1_entry.place(x=500,y=400)
        self.player2_entry=tk.Entry(self.window,width=20,font=("Helvetica",30))
        self.player2_entry.place(x=500,y=660)
        self.confirmation_button_entry=tk.Button(self.window,image=self.confirmation_button,borderwidth=0,command=self.play_squence)

        self.confirmation_button_entry.place(x=600,y=800)
    def play_squence(self):
        global player1_name
        global player2_name
        player1_name=self.player1_entry.get()
        player2_name=self.player2_entry.get()
        
        self.window.destroy()
    def run_multiplayer(self):
        
        manual_mode=Multiplayer(player1=player1_name,player2=player2_name)
        manual_mode.multiplayer_game_loop()
        


    def update(self):
        self.window.mainloop()
if __name__=="__main__":
    name_selector=Name_selection()
    name_selector.update()

    