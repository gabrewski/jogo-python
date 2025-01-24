class Item:
    def __init__(self, name, gold_value, equipable, consumable, tradable):
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.consumable = consumable
        self.tradable = tradable

class SaveLoadSystem:
    def __init__(self, filename):
        self.filename = filename

    def save_game(self, player, inventory):
        with open(self.filename, 'w') as file:
            file.write(f"Jogador:{player.name}\n")
            file.write(f"Level:{player.level}\n")
            file.write(f"HP:{player.hp}/{player.hp_max}\n")
            file.write(f"EXP:{player.exp}\n")
            file.write(f"Gold:{inventory.gold}\n")
            file.write("Inventory:\n")

            for item in inventory.player_items:
                file.write(f"{item.name},{item.gold_value},{item.equipable},{item.consumable},{item.tradable}\n")

    def load_game(self, player, inventory):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                lines = file.readlines()
                player.name = lines[0].split(":")[1].strip()
                player.level = int(lines[1].split(":")[1].strip())
                hp_values = lines[2].split(":")[1].strip().split("/")
                player.hp = int(hp_values[0])
                player.hp_max = int(hp_values[1])
                player.exp = int(lines[3].split(":")[1].strip())
                inventory.gold = int(lines[4].split(":")[1].strip())
                inventory.player_items = []

                for line in lines[6:]:
                    item_data = line.strip().split(",")
                    item = Item(name=item_data[0], 
                                gold_value=int(item_data[1]), 
                                equipable=item_data[2] == 'True', 
                                consumable=item_data[3] == 'True', 
                                tradable=item_data[4] == 'True')
                    inventory.player_items.append(item)

        except FileNotFoundError:
            print("Arquivo de salvamento não encontrado.")
        except ValueError as e:
            print(f"Erro ao carregar o jogo: {e}")
