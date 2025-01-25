from Entity.base_entity import Entity
from Entity.player import Player
from random import random
import time
from Item.item_list import potion1, potion2


def combat(player: 'Entity', enemy: 'Entity') -> bool:


    while True:
        print()
        option = int(input('ação -> ')) # placeholder (input do jogador)

        match option:
            case 1: # atacar
                if attack(attacker=player, target=enemy):
                    return stop_combat(victory=True)
            
            case 2: # defender
                if defend(defender=player, attacker=enemy):
                    continue
                else:
                    return stop_combat(victory=False)

            case 3: # curar
                heal(player)

            case 4: # fugir
                if flee():
                    print('Player fugiu') # placeholder
                    time.sleep(4)
                    return True
                else:
                    print('Fuga malsucedida') # placeholder
                    time.sleep(4)

        print() # placeholder
        # ação do inimigo
        if attack(attacker=enemy, target=player):
            return stop_combat(victory=False)



def attack(attacker: 'Entity', target: 'Entity') -> bool:
    atk_damage, crit = attacker.attack(target)

    if crit:
        print('crit dmg') # placeholder
    else:
        print('dmg') # placeholder
    print(f'{attacker.name}: {atk_damage} dmg') # placeholder

    return is_dead(target)


def defend(player: 'Entity', enemy: 'Entity') -> bool:
    def_damage, defend = player.defend(enemy)

    if defend:
        print('attack blocked') # placeholder
    else:
        print(f'defended and took {def_damage} dmg') # placeholder

    return not is_dead(player)


def heal(player: 'Entity'):
    potions = player.inventory.get_consumables()

    for i, pot in enumerate(potions): # placeholder
        print(i, pot) # placeholder
    choice = int(input('poção -> ')) #placeholder (input do jogador)

    selected_potion = potions[choice]
    heal_amount = selected_potion.hp_value
    player.hp += heal_amount
    player.inventory.remove_item(selected_potion)
    
    print(f'{heal_amount} healed') # placeholder


def flee() -> bool:
    return random.random() <= 0.7


def is_dead(entity: 'Entity') -> bool:
    return entity.hp == 0


def stop_combat(victory: bool) -> bool:
    print() # placeholder

    if victory:
        print('Player venceu') # placeholder
    else:
        print('Inimigo Venceu') # placeholder

    time.sleep(5) # placeholder
    return victory