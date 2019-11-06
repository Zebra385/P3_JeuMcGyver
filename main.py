#coding: utf-8 #encodage in French
import numpy as np
import Map as map_game

"""" This program is to star The Game Mac Gyver
"""

#try to read the file text maps.txt and transform in a array
def main():
    map1=map_game.Map("maps.txt")
    map1_df = map1.read_map
    print(map1_df)


if __name__ == "__main__":  # Main is to star the play like a programm
    main()