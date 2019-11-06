import Map as map_game
class GameManager:
    def __init__ (self):
        self.nom = "parcourt_jeu"
    def initialise(self):
        jeu = map_game.Map("maps.txt")
        jeu_df = jeu.read_map
        return jeu_df, print(jeu_df)


    @classmethod
    def start(cls):
        pass




def main():
    game_manager = GameManager.initialise
    print(map_df)#ne fonctionne pas
if __name__ == "__main__":  # Main is to star the play like a programm
    main()