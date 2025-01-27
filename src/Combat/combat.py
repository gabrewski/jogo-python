#combat_test.py
from Entity.enemy_list import enemy_list1, enemy_list2, enemy_list3, enemy_list4, enemy_list5
from Entity.base_entity import Entity
from Entity.enemy import Enemy
from random import random, choices
from typing import Callable
import time
import os


class CombatSystem:
    def __init__(self, game_window, txt_window, 
                 interface_func: Callable[[str], None], 
                 update_char: Callable, 
                 update_stats: Callable,
                 update_inv: Callable):
        
        self.game_window = game_window
        self.text_window = txt_window
        self.add_text = interface_func
        self.update_char = update_char
        self.update_stats = update_stats
        self.update_inventory = update_inv

        self.height, self.width = game_window.getmaxyx()


    def start_combat(self, player: 'Entity', enemy: 'Entity') -> bool:
        while True:
            self.update_enemy(enemy)
            self.add_text(pos=(1,2), text=f'Turno de {player.name}:')
            self.add_text(pos=(2,2), text=f'[1] Atacar       [2] Curar       [3] Fugir', clear=False)

            while True:
                option = self.text_window.getch()
                if option in [ord('1'), ord('2'), ord('3')]:
                    break

            match option-48:
                case 1: # atacar
                    win = self.attack(attacker=player, target=enemy)
                    self.update_enemy(enemy)
                    if win:
                        return self.stop_combat(player, enemy, victory=True)

                case 2: # curar
                    self.heal(player)

                case 3: # fugir
                    if self.flee(player, enemy):
                        return 'flee'

            self.add_text(text=f'Turno de {enemy.name}:')
            time.sleep(1.8)
            # ação do inimigo
            if self.attack(attacker=enemy, target=player):
                return self.stop_combat(player, enemy, victory=False)
        



    def attack(self, attacker: 'Entity', target: 'Entity') -> bool:
        atk_damage, crit = attacker.attack(target)

        self.add_text(pos=(1,2), text=f'Turno de {attacker.name}:')
        self.add_text((2, 2), f'{attacker.name} deu {atk_damage} de dano', clear=False)

        if crit:
            self.add_text((3,2), f'{attacker.name} acertou dano crítico!', clear=False)

        self.update_stats()
        time.sleep(2.5)

        return self.is_dead(target)


    def heal(self, player: 'Entity'):
        potions = list(set(player.inventory.get_consumables()))

        self.add_text(clear=True)

        for i, pot in enumerate(potions):
            self.add_text(pos=(i+1, 2), text=f'[{i+1}] {pot.name}: +{pot.hp_value} HP', clear=False)

        while True:
            option = self.text_window.getch()
            if option in [ord(str(i+1)) for i in range(len(potions))]:
                break

        selected_potion = potions[option-49]
        heal_amount = selected_potion.hp_value
        player.heal(selected_potion)

        self.add_text(text=f'{player.name} usou {selected_potion.name} e curou {heal_amount} HP')
        self.update_stats()
        time.sleep(3)


    def flee(self, player: 'Entity', enemy: 'Entity') -> bool:
        if random() <= 0.7:
            enemy.revive()
            self.add_text(text=f'{player.name} fugiu do combate...')
            time.sleep(3)
            return True
        else:
            self.add_text(text=f'A fuga de {player.name} falhou!')
            time.sleep(3)
            return False


    def is_dead(self, entity: 'Entity') -> bool:
        return entity.hp == 0


    def stop_combat(self, player, enemy, victory: bool) -> bool:
        if victory:
            lvl_up, exp_ganho = player.gain_exp(enemy.exp_range)
            gold_ganho = player.gain_gold(enemy.gold_range)

            self.add_text(text=f'{player.name} venceu o combate!')
            self.add_text(pos=(2,2), text=f'{player.name} ganhou {gold_ganho} de Gold', clear=False)
            self.add_text(pos=(3,2), text=f'{player.name} ganhou {exp_ganho} de exp', clear=False)

            if lvl_up:
                self.add_text(pos=(4,2), text=f'{player.name} subiu de nível!', clear=False)

            self.update_stats()
            self.update_char()

        else:
            gold_perdido = player.inventory.gold // 2
            player.inventory.gold -= gold_perdido
            self.add_text(pos=(1,2), text=f'{enemy.name} venceu o combate...')
            self.add_text(pos=(2,2), text=f'{player.name} perdeu {gold_perdido} Gold e foi carregado de volta para a vila', clear=False)

            self.update_stats()
            self.update_char()
            player.revive()

        enemy.revive()
        self.update_inventory()
        time.sleep(4)
        self.add_text(clear=True)
        return victory
    

    def get_random_enemy(self, stage:int) -> 'Enemy':
        match stage:
            case 1:
                enemy_list = enemy_list1
            case 2:
                enemy_list = enemy_list2
            case 3:
                enemy_list = enemy_list3
            case 4:
                enemy_list = enemy_list4
            case 5:
                enemy_list = enemy_list5

        enemies, weigths = zip(*enemy_list)
        return choices(enemies, weigths).pop()
    

    def update_enemy(self, enemy):
        height = self.height//2
        width = (self.width//2)-10

        self.game_window.clear()
        self.game_window.box()
        self.game_window.addstr(height-1, width, f'{(enemy.name).center(20)}')
        self.game_window.addstr(height+1, width, f'HP: {enemy.hp}')
        self.game_window.addstr(height+2, width, f'ATK: {enemy.atk_value + enemy.weapon.atk_value}')
        self.game_window.addstr(height+3, width, f'DEF: {enemy.armor.def_value}')
        self.game_window.addstr(height+4, width, f'CRIT_CHANCE: {enemy.crit_chance}')
        self.game_window.addstr(height+5, width, f'CRIT_DAMAGE: {enemy.crit_damage}')
        self.game_window.refresh()
