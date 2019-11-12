# coding: utf-8 # encodage in French

"""
Create a class Map to play , the map is a file text that transform in a array[line, column], name map_structure
"""


class Map:
    def __init__(self, file):
        self.file = file
        self.map_structure = []  # My array to map
        with open(self.file) as f:  # Method open can read the text in the file
            lines = f.readlines()  # Method readlines to seperate ligne of the text
            for line in lines:
                #line = line.split(line)
                line = line.strip()  # strip
                self.map_structure.append(list(line)) #  Add list line in list  map_structure
            f.close()
     #A revoir ne fonctionne plus
    #def __str__(self):  # We change the "print", to can write the map like a array
     #   return "\n".join(self.map_structure)

    def trouve_un_character(self, character):  # determinate the position to a character m to My Gyver and g to  Guard
        self.character = str(character)
        x_character = int()
        y_character = int()
        for i in range(0,14):
            for j in range(0,14):
                if self.map_structure[i][j] == character:
                    x_character = int(i)
                    y_character = int(j)
        return (x_character, y_character)  #return the position of the character

