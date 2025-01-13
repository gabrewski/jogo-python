from item import *

class Inventario:
    def __init__(self, slots: int, gold: int, player_items: list) <- None:
        self.slots = slots
        self.gold = gold
        self.player_items = player_items
    
    def add_item(self,item) -> None:
        if self.slots > len(self.player_items):
            self.player_items.append(item)
        else:
            print("Seu inventário está cheio.")
    
    def sell_item(self, item) -> None:
        if len(self.player_items) > 0:
            self.player_items.pop(item)
            self.gold += item.gold_value
        else:
            print("Você não possui itens no seu inventário.")

    '''def discard_item(self, item) -> None:
        print("Itens no inventário:\n")
        for index, item in enumerate(self.player_items, start=1):
            print(f"{index}. {item}")
        discard = input("Qual item deseja descartar? ")
        ???
        self.player_items.pop(item)
    '''

    def get_item(self):
        print("Itens no inventário: ")
        return self.player_items

inventario_player = Inventario(slots = 15, gold = 0, player_items = [])


#integrar com combate
