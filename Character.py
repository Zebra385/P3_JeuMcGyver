
class Character:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position ) = y_position



class MyGyver(Character):
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position ) = y_position \
    #method to move m like My Gyver
    @ classmethod
     def move(cls, x_position, y_position):
        x = x_position
        y = y_position
        if key="fleche top":
            y += 1
        elif key="fleche down":
            y -= 1
        if key="fleche right":
            x += 1
        elif key="flecheleft":
                x -= 1
 class Guard(Character):
            def __init__(self, x_position, y_position):
                self.x_position = x_position
                self.y_position ) = y_position

def main():
     my_gyver = Mygyver(x_map_begining,y_map_begining)
     guard = Guard(_map_end,y_map_dnd)