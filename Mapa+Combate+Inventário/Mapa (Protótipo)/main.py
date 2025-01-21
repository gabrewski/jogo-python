from map import *
import os 

os.system("cls")
def run() -> None:
    while True:
        game_map.display_map()
        input("> ")

if __name__ == "__main__":
    map_larg, map_alt = 60, 15
    game_map = Map(map_larg, map_alt)
    run()


#To do list:
#Ser capaz de movimentar personagem pelo mapa
#Ser capaz de iniciar combate com uma chance aleatória no mundo aberto
#Implementar modelo de exploração:
#>Revelar mapa aos poucos com um sistema de FOV (Field of View)
#>Implementar legenda de mapa
#Segmentar algoritmo de geração de mapa entre fases