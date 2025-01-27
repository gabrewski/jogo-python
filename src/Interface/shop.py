from Item.item_list import *
from Item.inventory import Inventory
import curses

class Shop:
    def __init__(self, player, name, items, level_requirements):
        self.player = player
        self.name = name
        self.items = items
        self.level_requirements = level_requirements

    def get_available_items(self, player_level):
        """Retorna itens disponíveis baseado no nível do jogador"""
        return [
            item for item in self.items 
            if self.level_requirements.get(item.name, float('inf')) <= player_level
        ]

    def display_shop(self, window, player_level):
        """Mostra itens disponíveis para compra"""
        available_items = self.get_available_items(player_level)
        height, width = window.getmaxyx()
        
        window.clear()
        window.box()

        instructions = "Pressione número para comprar ou 'Q' para voltar"

        if not available_items:
            msg = "Nenhum item disponível no momento."
            window.addstr(height//2, (width - len(msg))//2, msg)
            window.addstr(height-2, (width - len(instructions))//2, instructions)
            window.refresh()
            return None
        
        title = f"Loja de {self.name}"
        gold_info = f"Seu ouro: {self.player.inventory.gold}"
        window.addstr(1, (width - len(title))//2, title)
        window.addstr(2, (width - len(gold_info))//2, gold_info)

        start_y = (height - len(available_items)) // 2

        for i, item in enumerate(available_items, 0):
            item_text = f"{i+1}. {item.name} - {item.gold_value} gold"
            window.addstr(start_y + i, (width - len(item_text))//2, item_text)

        
        window.addstr(height-2, (width - len(instructions))//2, instructions)
        window.refresh()

        return available_items

    def buy_item(self, window, player_gold, choice, available_items):
        height, width = window.getmaxyx()

        if 1 <= choice <= len(available_items):
            selected_item = available_items[choice - 1]
            
            if player_gold >= selected_item.gold_value:
                self.player.inventory.gold -= selected_item.gold_value
                self.player.inventory.add_item(selected_item)
                msg = f"Você comprou {selected_item.name}!"
            else:
                msg = "Ouro insuficiente!"
        else:
            msg = "Escolha inválida!"
        
        window.addstr(height-3, (width - len(msg))//2, msg)
        window.refresh()
        curses.napms(1000)


def open_weapon_shop(window, player, update_inv):
    weapon_shop = Shop(player, "Forja", 
        [espada1, espada2, espada3, porrete, adaga, arco, machado, cimitarra, clava_gelo, espada_flamejante],
        {"Espada de Ferro": 1, "Espada de Aço": 3, "Espada Longa": 4, "Porrete de Madeira": 1, 
         "Adaga de Aço": 2, "Arco e Flecha": 3, "Machado": 4, "Cimitarra": 6, "Clava de Gelo": 7, "Espada Flamejante": 8}
    )
    handle_shop(window, player, weapon_shop, update_inv)

def open_armor_shop(window, player, update_inv):
    armor_shop = Shop(player, "Ferraria", 
        [armor1, armor2, armor3, armor4],
        {"Armadura de Ferro": 2, "Armadura de Aço": 4, "Armadura de Platina": 6, "Armadura Divina": 8}
    )
    handle_shop(window, player, armor_shop, update_inv)

def open_potion_shop(window, player, update_inv):
    potion_shop = Shop(player, "Poções", 
        [potion1, potion2, potion3, potion4],
        {"Poção Revigorante": 1, "Poção de Cura Leve": 3, "Poção de Cura Poderosa": 5, "Poção de Cura Suprema": 7}
    )
    handle_shop(window, player, potion_shop, update_inv)

def handle_shop(window, player, shop, update_inv):
    available_items = None
    while True:
        if available_items is None:
            available_items = shop.display_shop(window, player.level)
        
        key = window.getch()
        if key == ord('q') or key == ord('Q'):
            break
        elif ord('1') <= key <= ord('9'):
            shop.buy_item(window, player.inventory.gold, 
                         key - ord('0'), available_items)
            update_inv()
            available_items = shop.display_shop(window, player.level)