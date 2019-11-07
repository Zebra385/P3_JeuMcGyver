#coding: utf-8 #encodage in French
import numpy as np
import Map as map_game
from GameManager import GameManager

"""" This program is to star The Game Mac Gyver
"""

#try to read the file text maps.txt and transform in a array
def main():

    game = GameManager()
    game.start()
    #print("la position de Mc Gyver est", x_character, y_character)


if __name__ == "__main__":  # Main is to star the play like a programm
    main()