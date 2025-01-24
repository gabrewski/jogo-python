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

    def discard_item(self, items):
        while True:
            try:
                print("Itens no inventário:")
                for index, item in enumerate(items, start=1):
                    print(f"{index}. {item}")
                discard = int(input("\nQual item deseja descartar? "))
                if 1 <= discard <= len(items):
                    opt = input(f"Deseja descartar o item '{items[discard - 1]}'? Sim (S) / Não (N): ").strip().lower() #limpam o input
                    if opt == 's':
                        removed_item = items.pop(discard - 1)
                        print(f"Item '{removed_item}' foi descartado.")
                        if items: #se ainda houver itens na lista
                            continue_discard = input("Deseja descartar outro item?  Sim (S) / Não (N): ").strip().lower()
                            if continue_discard != 's':
                                print("Operação encerrada.")
                                break
                        else:
                            print("Todos os itens foram descartados.")
                            break
                    elif opt == 'n':
                        print("Operação cancelada.")
                    else:
                        print("Opção inválida. Tente novamente.")
                else:
                    print("Por favor, insira um número correspondente ao item.")
            except ValueError:
                print("Por favor, insira um número correspondente ao item.")   

    def get_item(self):
        print("Itens no inventário: ")
        return self.player_items
    

    def get_consumables(self) -> list['Item']:
        '''Retorna uma lista com todos os itens consumíveis (poções) do inventário.'''
        return [item for item in self.player_items if item.consumable]

    
    def options(self):
        print("O que deseja fazer")