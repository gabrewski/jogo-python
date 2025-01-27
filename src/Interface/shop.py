from Item.item_list import *
from Item.inventory import Inventory

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

    def display_shop(self, player_level):
        """Mostra itens disponíveis para compra"""
        available_items = self.get_available_items(player_level)
        
        if not available_items:
            print("Nenhum item disponível no momento.")
            return None
        
        print(f"Loja de {self.name}:")
        for i, item in enumerate(available_items, 1):
            print(f"{i}. {item.name} - Valor: {item.gold_value} gold")
        
        return available_items

    def buy_item(self, player_level, player_gold, choice):
        """Processa a compra de item"""
        available_items = self.get_available_items(player_level)
        
        if not available_items:
            print("Nenhum item disponível para compra.")
            return None
        
        if 1 <= choice <= len(available_items):
            selected_item = available_items[choice - 1]
            
            if player_gold >= selected_item.gold_value:
                self.player.inventory.gold -= selected_item.gold_value
                self.player.inventory.add_item(selected_item)
                print(f"Você comprou {selected_item.name}!")
                return selected_item
            else:
                print("Ouro insuficiente para comprar este item.")
                return None
        else:
            print("Escolha inválida.")
            return None

def village_menu(player):
    """Menu principal da vila com diferentes lojas"""
    weapon_shop = Shop(player, "Forja", 
        [espada1, espada2, espada3, porrete, adaga, arco, machado, cimitarra, clava_gelo, espada_flamejante],
        {"Espada de Ferro": 1, "Espada de Aço": 3, "Espada Longa": 4, "Porrete de Madeira": 1, 
         "Adaga de Aço": 2, "Arco e Flecha": 3, "Machado": 4, "Cimitarra": 6, "Clava de Gelo": 7, "Espada Flamejante": 8}
    )
    
    armor_shop = Shop(player, "Ferraria", 
        [armor1, armor2, armor3, armor4],
        {"Armadura de Ferro": 2, "Armadura de Aço": 4, "Armadura de Platina": 6, "Armadura Divina": 8}
    )
    
    potion_shop = Shop(player, "Poções", 
        [potion1, potion2, potion3, potion4],
        {"Poção Revigorante": 1, "Poção de Cura Leve": 3, "Poção de Cura Poderosa": 5, "Poção de Cura Suprema": 7}
    )

    while True:
        print("\n--- Bem-vindo à Vila ---")
        print("Seu ouro:", player.inventory.gold)
        print("1. Forja")
        print("2. Ferraria")
        print("3. Poções")
        print("0. Sair")
        
        try:
            choice = int(input("Escolha uma loja: "))
            
            if choice == 0:
                break
            elif choice == 1:
                items = weapon_shop.display_shop(player.level)
                if items:
                    buy_choice = int(input("Escolha um item para comprar (0 para voltar): "))
                    if buy_choice > 0:
                        weapon_shop.buy_item(player.level, player.inventory.gold, buy_choice)
            elif choice == 2:
                items = armor_shop.display_shop(player.level)
                if items:
                    buy_choice = int(input("Escolha um item para comprar (0 para voltar): "))
                    if buy_choice > 0:
                        armor_shop.buy_item(player.level, player.inventory.gold, buy_choice)
            elif choice == 3:
                items = potion_shop.display_shop(player.level)
                if items:
                    buy_choice = int(input("Escolha um item para comprar (0 para voltar): "))
                    if buy_choice > 0:
                        potion_shop.buy_item(player.level, player.inventory.gold, buy_choice)
            else:
                print("Opção inválida.")
        
        except ValueError:
            print("Por favor, insira um número válido.")