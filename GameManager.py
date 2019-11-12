from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item


"""
Create class GameManager to star the game

"""
class GameManager:
    def __init__(self):
        self.map = Map("maps.txt")
        (x_pos_bigining, y_pos_bigining) = self.map.trouve_un_character("m")  # We looking for for position of Mc Gyver with is charater special m
        #  Test: print("la position de Mc Gyver est", x_pos_bigining, y_pos_bigining)
        (x_pos_end, y_pos_end) = self.map.trouve_un_character("g")  # We looking for for position of Guard with is charater special g
        print("la position du guard est ligne  ", x_pos_end, ", et colonne  ", y_pos_end)
        self.mcgyver = McGyver(x_pos_bigining, y_pos_bigining)
        # mcgyver.x_position, mcgyver.y_position= x_pos_bigining, y_pos_bigining
        self.guard = Guard(x_pos_end, y_pos_end)
        self.items = [Item("e", "Ether",-1,-1), Item("n", "Needle",-1,-1) , Item("p", "Pipe",-1,-1)]
        empty_spaces = self.map.find_all_characters(" ")
        for item in self.items:
            position = choice(empty_spaces)# random
            item.set_position(position[0], position[1]) #on definit une position sur la map
            self.map.write_character(item.character, item.x, item.y) # on met les objets sur la map

    def start(self):
        print(self.map)

        #guard.x_position,guard.y_position = x_pos_end, y_pos_end
        #  Test print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        #  Test print("la position du guard est ligne  ", guard.x_position,", et colonne  ", guard.y_position)
        #  We add in the map 3 random objects
        c = 0
        #while c != 3:
         #   i = randint(0,7)
          #  j = randint(0,14)
           # if self.map.map_structure[i][j] == " ":
            #    self.map.map_structure[i][j] = "o"
             #   c += 1
        #test for i in range(0,14):
            #for j in range(0,14):
             #   print("en ligne i :", i,"en colonne :",j,"le caracere est:",self.map.map_structure[i][j])

        compteur_objet = 0
        while (self.mcgyver.x_position, self.mcgyver.y_position) != (self.guard.x_position, self.guard.y_position):
            #  Window map
            print(self.map)
            x_position, y_position = self.mcgyver.move(self.mcgyver.x_position, self.mcgyver.y_position)
            #  Test print("le caracter de character.character est :",character_rien.character)
            if  self.map.map_structure[x_position][y_position] == " " or self.map.map_structure[x_position][y_position] == "g" or self.map.map_structure[x_position][y_position] == "o":
                if self.map.map_structure[x_position][y_position] == "o":
                    compteur_objet +=1
                self.map.map_structure[self.mcgyver.x_position][self.mcgyver.y_position] = "m"
                # Test print("le caracter est Mc  position:", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
                self.mcgyver.x_position, self.mcgyver.y_position = x_position, y_position
                #  Test print("le caracter est :", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
            else:
                print(" No, You can't go here")
                x_position, y_position = self.mcgyver.x_position, self.mcgyver.y_position
            # Test print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        if compteur_objet == 3 :
            print("YOU ARE A WINNER")
        else:
            print("Sorry but you haven't the three object: YOU LOSE")
