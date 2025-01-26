#test_combat.py

from Combat.combat_interface import start_combat
from Entity.enemy_list import *
from Entity.player import Player
from Item.item_list import potion1, potion2, potion3  # Importar as poções

def main():
    # Inicializa o jogador com stats básicos
    player = Player(
        name="Herói",
        hp=5000,  # HP menor para testar cura
        atk_value=20,
        crit_chance=0.2,
        crit_damage=1.5
    )
    
    # Adiciona poções ao inventário
    player.inventory.player_items.extend([
        potion1,
        potion2,
        potion3
    ])
    
    # Configura quantidades (se necessário)
    potion1.quantity = 3
    potion2.quantity = 2
    potion3.quantity = 1
    
    # Inicia o combate
    start_combat(player, mestre_aranhas)

if __name__ == "__main__":
    main()