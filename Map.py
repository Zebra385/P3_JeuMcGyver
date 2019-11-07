import numpy as np
import pandas as pd
"""
Create a maps to play , the map is a file textthat transform in a array[line, column]
"""

class Map:
    def __init__(self,file):
        self.file = file
        self.map_structure = []
        with open(self.file) as f:
            lines = f.readlines()
            for line in lines :
                line = line.strip()#strip
                self.map_structure.append(line)

    def __str__(self):
         #for line in self.map_structure:
           #print(line)
        return "\n".join(self.map_structure)

    # read the file text and transform this in a  numpy array with the module numpy

    #determinate the position to a character m = My Gyver et g= Guard

    def trouve_un_character(self, character):
        self.character = str(character)
        for i, line in enumerate(self.map_structure):
            for j, c in enumerate(self.map_structure):
        # ou est Mc Gyver, Il faut trouver ou est le m
                if self.map_structure[i][j] == character:
                    x_character = int(i)
                    y_character = int(j)
        return (x_character, y_character)
        #print(character, "est sur la ligne: :", x_map_MyGyver,"et sur la colonne : " y_map_Mygyver)







