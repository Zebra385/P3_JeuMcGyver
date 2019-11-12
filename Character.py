"""
Create a class Character with attribute a position: x_position for index of line
and y_position for index of column
"""

class Character:
    def __init__(self, character, x_position, y_position):
        self.character = character
        self.x_position = x_position
        self.y_position = y_position

"""
Create  class McGyver those are a children-class Character with special character = m
"""


class McGyver(Character):
    def __init__(self, character, x_position, y_position):
        Character.__init__(self, character, x_position,y_position)
        self.character= "m"
        self.x_position = x_position
        self.y_position = y_position

    """
    Method move to move m like My Gyver with keyboard
    z to up, s:  down, q : left and  d : right
    """

    def move(self, x_position, y_position):
        self.x_position= x_position
        self.y_position = y_position
        keyboard = input("Tell me how you want  move Mc Gyver; the key z to up, s:  down, q : left and  d : right ")
        if keyboard =='z':  # if key 'z' is pressed
            x_position -= 1
            return x_position, y_position
        elif keyboard == 's':
            x_position += 1
            return x_position, y_position
        if keyboard == 'q':
            y_position -= 1
            return x_position, y_position
        elif keyboard == 'd':
            y_position += 1
            return x_position, y_position

"""
Create  class Guard those are a children-class Character with special character = g
"""


class Guard(Character):
    def __init__(self, character, x_position, y_position,):
        Character.__init__(self, character, x_position, y_position)
        self.character = "g"
        self.x_position = x_position
        self.y_position = y_position

