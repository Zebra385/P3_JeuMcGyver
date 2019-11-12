from random import randint
from Map import Map
from Character import Character
from Character import McGyver
from Character import Guard


"""
Create class GameManager to star the game

"""
class GameManager:
    def __init__(self):
        self.map = Map("maps.txt")


    def start(self):
        print(self.map.map_structure)
        (x_pos_bigining, y_pos_bigining) = self.map.trouve_un_character("m")#We looking for for position of Mc Gyver with is charater special m
        #  Test: print("la position de Mc Gyver est", x_pos_bigining, y_pos_bigining)
        (x_pos_end, y_pos_end) = self.map.trouve_un_character("g") #We looking for for position of Guard with is charater special g
        print("la position du guard est ligne  ", x_pos_end, ", et colonne  ", y_pos_end)
        mcgyver = McGyver("m",x_pos_bigining, y_pos_bigining)
        mcgyver.x_position, mcgyver.y_position= x_pos_bigining, y_pos_bigining
        guard = Guard("g",x_pos_end, y_pos_end)
        guard.x_position,guard.y_position = x_pos_end, y_pos_end
        #  Test print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        #  Test print("la position du guard est ligne  ", guard.x_position,", et colonne  ", guard.y_position)
        #  We add in the map 3 random objects
        c = 0
        while c != 3:
            i = randint(0,7)
            j = randint(0,14)
            if self.map.map_structure[i][j] == " ":
                self.map.map_structure[i][j] = "o"
                c += 1
        #test for i in range(0,14):
            #for j in range(0,14):
             #   print("en ligne i :", i,"en colonne :",j,"le caracere est:",self.map.map_structure[i][j])

        compteur_objet = 0
        while (mcgyver.x_position,mcgyver.y_position) != (guard.x_position, guard.y_position):
            #  Window map
            print(self.map.map_structure)# A corriger car ne s'affiche pas en tableau
            x_position, y_position = mcgyver.move(mcgyver.x_position, mcgyver.y_position)
            #  Test print("le caracter de character.character est :",character_rien.character)
            if  self.map.map_structure[x_position][y_position] == " " or self.map.map_structure[x_position][y_position] == "g" or self.map.map_structure[x_position][y_position] == "o":
                if self.map.map_structure[x_position][y_position] == "o":
                    compteur_objet +=1
                self.map.map_structure[mcgyver.x_position][mcgyver.y_position] = "m"
                # Test print("le caracter est Mc  position:", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
                mcgyver.x_position, mcgyver.y_position = x_position, y_position
                #  Test print("le caracter est :", self.map.map_structure[mcgyver.x_position][mcgyver.y_position])
            else:
                print(" No, You can't go here")
                x_position, y_position = mcgyver.x_position, mcgyver.y_position
            # Test print("la position de Mc Gyver est ligne ", mcgyver.x_position,", et colonne ", mcgyver.y_position)
        if compteur_objet == 3 :
            print("YOU ARE A WINNER")
        else:
            print("Sorry but you haven't the three object: YOU LOSE")
