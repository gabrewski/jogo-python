from map_forest import Map
from character import Player
import os

os.system("")


def run() -> None:
    player = Player(name="Player", health=100)
    player.pos = [map_w // 2, map_h // 2]  # start in the middle of the map
    game_map.update_map(player.pos, player.marker)  #place the player's marker on the map

    while True:
        os.system("cls" if os.name == "nt" else "clear")  #clear the console for a cleaner display
        game_map.display_map()  #display th e map with the player position

        player.calculate_movement_options(map_w, map_h)
        
        print("Movement Options:")
        game_map.display_movement_options(player.movement_options)
        
        #get movement input from the player and move them
        player.get_movement_input()
        
        #update the map with the new player position
        game_map.update_map(player.pos, player.marker)

if __name__ == "__main__":
    map_w, map_h = 45, 15  # Define map width and height
    game_map = Map(map_w, map_h)  # Create the map
    run()