
class Character:
    def __init__(self, character, x_position, y_position):
        self.character = character
        self.x_position = x_position
        self.y_position = y_position



class MyGyver(Character):
    def __init__(self, character, x_pos, y_pos,x_pos_bigining, y_pos_begining):
        Character.__init__(self, character, x_pos,y_pos)
        self.character= "m"
        self.x_position_bigining = x_pos_bigining
        self.y_position_bigining =  y_pos_begining

    #method to move m like My Gyver

     def move(self, x_position, y_position) :
        x.self = x_position
        y.sef = y_position
        if key="fleche top":
            y -= 1
        elif key="fleche down":
            y += 1
        if key="fleche right":
            x += 1
        elif key="flecheleft":
                x -= 1
 class Guard(Character):
    def __init__(self, character, x_position, y_position,x_pos_end, y_pos_end):
        Character.__init__(self, character, x_pos, y_pos)
        self.character = "g"
        self.x_position_end = x_pos_end
        self.y_position_end = y_pos_end

