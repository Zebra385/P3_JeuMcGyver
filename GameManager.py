from Map import Map
from Character import Character
from Character import McGyver
from Character import Guard

class GameManager:
    def __init__(self):
        self.map = Map("maps.txt")


    def start(self):
        print(self.map)
        (x_pos_bigining, y_pos_bigining) =self.map.trouve_un_character("m")#We looking for for position of Mc Gyver with is charater special m
        #print("la position de Mc Gyver est", x_pos_bigining, y_pos_bigining)
        (x_pos_end, y_pos_end) = self.map.trouve_un_character("g") #We looking for for position of Guard with is charater special g
        mcgyver = McGyver("m",x_pos_bigining, y_pos_bigining)
        mcgyver.x_position, mcgyver.y_position= x_pos_bigining, y_pos_bigining
        guard=Guard("g",x_pos_end, y_pos_end)
        guard.x_position,guard.y_position = x_pos_end, y_pos_end
        print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        print("la position du guard est ligne  ", guard.x_position,", et colonne  ", guard.y_position)
        while (mcgyver.x_position,mcgyver.y_position) != (guard.x_position, guard.y_position):
            #affichage map
            print(self.map)
            x_position, y_position = mcgyver.move(mcgyver.x_position, mcgyver.y_position)
            character_rien= Character(" ", mcgyver.x_position, mcgyver.y_position)
            character_g = Character("g", mcgyver.x_position, mcgyver.y_position)
            #test print("le caracter de character.character est :",character_rien.character)
            if  self.map.map_structure[x_position][y_position] == character_rien.character or self.map.map_structure[x_position][y_position] == character_g.character:
                self.map.map_structure[mcgyver.x_position][mcgyver.y_position] == "m"
                # test print("le caracter est Mc  position:", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
                mcgyver.x_position, mcgyver.y_position = x_position, y_position
                #test print("le caracter est :", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
            else:
                print(" Non tu ne peux pas aller là")
                x_position, y_position = mcgyver.x_position, mcgyver.y_position
            # test print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        print("YOU ARE A WINNER")
