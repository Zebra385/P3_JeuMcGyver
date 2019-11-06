import numpy as np
import pandas as pd
"""
Create a maps to play , the map is a file textthat transform in a array[line, column]
"""

class Map:
    def __init__(self,file):
        self.file = file
    # read the file text and transform this in a  numpy array with the module numpy
    @property
    def read_map(self):
        map = np.genfromtxt(self.file, str, delimiter="\n")
        map_df = pd.DataFrame(map)
        return map_df
    #determinate the position to a character m = My Gyver et g= Guard
    @property
    def trouve_un_character(self, character):
        self.character = str(character)
        # ou est Mc Gyver, Il faut trouver ou est le m
        for i in range(0,len(self.map_df)):
          for j  in range(0,len(self.map_df)):
               if map[i][j] == character:
                    x_map_MyGyver = int(i)
                    y_map_Mygyver = int(j)
        return x_map_MyGyver#, y_map_Mygyver
        #print(character, "est sur la ligne: :", x_map_MyGyver,"et sur la colonne : " y_map_Mygyver)





if __name__ == "__main__":  # Main is to star the play like a module

    read_map(self)#quoi mettre ici