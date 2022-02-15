class Game():
    def __init__(self,gameName):
        self.gameName = gameName

    def display(self):
        for game in self.gameName:
            print(game)

    def playGame(self, play):
        if play in self.gameName:
            print(f"you've selected {play} game to play")
            self.gameName.remove(play)
        else:
            print(f"sorry this {play} game isn't avilable")

    def returnGame(self,play):
        self.gameName.append(play)
        print("thanks for playing this game")

class player():
     def inputPLay(self):
         self.game=input("enter a game name to play: ")
         return self.game

     def input2PLay(self):
         self.game=input("enter a game name to return it: ")
         while(self.game != "GTA V" or "red dead 2" or "far cry 6" or "watch dogs" or "forza horizon 5" or "cyberpunk"):
               #if self.game != "GTA V" or "red dead 2" or "far cry 6" or "watch dogs" or "forza horizon 5" or "cyberpunk":
                print("invalid game name")
                self.game=input("enter a  valid game name to return it: ")
                return self.game
         return self.game

aaa= Game(["GTA v","red dead 2","far cry 6","watch dogs", "forza horizon 5", "cyberpunk"])
play=player()
while(True):
    digi='''===== OPEN WORLD GAMES =====
    1)PRESS 1 FOR TO DISPLAY LIST OF GAMES:
    2)PRESS 2 FOR TO PLAY THE GAME:
    3)PRESS 3 FOR TO RETURN THE GAME:
    4)PRESS 4 TO EXIT IT:'''
    print(digi)
    screen=int(input("enter a number :"))

    if screen==1:
        aaa.display()
    elif screen==2:
        aaa.playGame(play.inputPLay())
    elif screen==3:
        aaa.returnGame(play.input2PLay())
    elif screen==4:
        exit()
    else:
        print("invalid code")


