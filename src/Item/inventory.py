#inventory.py

from Item.category import *


class Inventory:
    def __init__(self, slots: int = 15, gold: int = 0, player_items: list = []):
        self.slots = slots
        self.gold = gold
        self.player_items = player_items
    

    def add_item(self,item) -> None:
        if self.slots > len(self.player_items):
            self.player_items.append(item)
        else:
            print("Seu inventário está cheio.")
    

    def sell_item(self, item):
        if len(self.player_items) > 0:
            self.player_items.pop(item)
            self.gold += item.gold_value
        else:
            print("Você não possui itens no seu inventário.")
    

    def get_consumables(self) -> list['Item']:
        '''Retorna uma lista com todos os itens consumíveis (poções) do inventário.'''
        return [item for item in self.player_items if item.consumable]
    

    def remove_item(self, item: 'Item'):
        self.player_items.remove(item)