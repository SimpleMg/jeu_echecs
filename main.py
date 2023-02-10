from mesClasses import *


if __name__ == '__main__':
    player_1 = Player(input("entrez ton pseudo: \n"))
    player_2 = Player(input("entrez ton pseudo: \n"))
    satrt_game = MyGame(player_1, player_2)
