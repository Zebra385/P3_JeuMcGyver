from Map import Map


class GameManager:
    def __init__(self):
        self.map = Map("maps.txt")

    def initialise(self):
        jeu = map_game.Map("maps.txt")
        jeu_df = jeu.read_map
        return jeu_df, print(jeu_df)

    def start(self):
        #x_pos_bigining, y_pos_bigining = 0,0
        #x_pos_end, y_pos_end = 0, 0
        print(self.map)
        #(x_pos_bigining, y_pos_bigining) =self.map.trouve_un_character("m")
        print("la position de Mc Gyver est", self.map.trouve_un_character("m"))
        print(self.map)
        #(x_pos_end, y_pos_end) = self.map.trouve_un_character("g")
        print("la position du guard est", self.map.trouve_un_character("g"))
        pass
