"""
Create a maps to play , the map is a file text that transform in a array[line, column]
"""


class Map:
    def __init__(self, file):
        self.file = file
        self.map_structure = []  # My array to map
        with open(self.file) as f:  # Method open can read the text in the file
            lines = f.readlines()  # Method readlines to seperate ligne of the text
            for line in lines:
                line = line.strip()  # strip
                self.map_structure.append(line)

    def __str__(self):  # We change the "print", to can write the map like a array
        return "\n".join(self.map_structure)

    def trouve_un_character(self, character):  # determinate the position to a character m to My Gyver and g to  Guard
        self.character = str(character)
        for i, line in enumerate(self.map_structure):
            for j, c in enumerate(self.map_structure):
                if self.map_structure[i][j] == character:
                    x_character = int(i)
                    y_character = int(j)
        return (x_character, y_character)
