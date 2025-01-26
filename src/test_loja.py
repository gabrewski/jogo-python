import curses
from Item.item_list import armor_loja, weapon_loja, potion_loja

class Loja:
    def __init__(self, largura: int, altura: int, player_inventory: dict): 
        self.largura = largura
        self.altura = altura
        self.player_inventory = player_inventory
        if 'gold' not in self.player_inventory:
            self.player_inventory['gold'] = 0
        # Structure: {category: {item_name: quantity}}
        self.shop_inventory = {
            'armaduras': {item.name: {'item': item, 'quantity': 5} for item in armor_loja},
            'armas': {item.name: {'item': item, 'quantity': 5} for item in weapon_loja},
            'itens de cura': {item.name: {'item': item, 'quantity': 5} for item in potion_loja}
        }

    def mostrar_loja(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Bem-vindo à loja!")
            stdscr.addstr(1, 0, f"Gold: {self.player_inventory['gold']}")
            stdscr.addstr(3, 0, "O que deseja fazer?")
            stdscr.addstr(4, 0, "1. Comprar armaduras")
            stdscr.addstr(5, 0, "2. Comprar armas")
            stdscr.addstr(6, 0, "3. Comprar itens de cura")
            stdscr.addstr(7, 0, "4. Sair")
            stdscr.refresh()

            key = stdscr.getch()

            if key == ord('1'):
                self.comprar_categoria(stdscr, 'armaduras')
            elif key == ord('2'):
                self.comprar_categoria(stdscr, 'armas')
            elif key == ord('3'):
                self.comprar_categoria(stdscr, 'itens de cura')
            elif key == ord('4'):
                self.vender_itens(stdscr)
            elif key == ord('5'):
                break

    def comprar_categoria(self, stdscr, categoria):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Escolha o item para comprar ({categoria}):")
        stdscr.addstr(1, 0, f"Gold: {self.player_inventory['gold']}")
        items = list(self.shop_inventory[categoria].items())
        y_offset = 2 

        for idx, item_data in enumerate(items, start=1):
            item = item_data[1]['item']
            stdscr.addstr(y_offset, 0, f"{idx}. {item.name} - Preço: {item.gold_value} (Quantidade: {item_data[1]['quantity']})")
            y_offset += 1

        stdscr.addstr(y_offset + 1, 0, "Digite o número do item ou '0' para voltar:")
        stdscr.refresh()

        try:
            input_str = self.get_input(stdscr, y_offset + 2, 0)
            choice = int(input_str)
            if choice == 0:
                return
            if 1 <= choice <= len(items):
                selected_name, selected_data = items[choice - 1]
                item_selecionado = selected_data['item']  # Obter o item correto
                if selected_data['quantity'] > 0 and self.player_inventory['gold'] >= item_selecionado.gold_value:
                    self.player_inventory['gold'] -= item_selecionado.gold_value  # Usar o preço do item selecionado
                    selected_data['quantity'] -= 1
                    self.player_inventory[item_selecionado.name] = self.player_inventory.get(item_selecionado.name, 0) + 1
                    stdscr.addstr(y_offset + 3, 0, f"Você comprou {selected_name}!")
                elif self.player_inventory['gold'] < item.gold_value:
                    stdscr.addstr(y_offset + 3, 0, "Gold insuficiente!")
                else:
                    stdscr.addstr(y_offset + 3, 0, "Item esgotado!")
            else:
                stdscr.addstr(y_offset + 3, 0, "Opção inválida!")
        except ValueError:
            stdscr.addstr(y_offset + 3, 0, "Entrada inválida!")
        stdscr.refresh()
        stdscr.getch()


    def get_input(self, stdscr, y, x):
        input_str = ""
        while True:
            stdscr.addstr(y, x, " " * 20)
            stdscr.addstr(y, x, input_str)
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                break
            elif key == curses.KEY_BACKSPACE or key == 127:
                input_str = input_str[:-1]
            else:
                input_str += chr(key)
        return input_str


def iniciar_loja(player_inventory):
    loja = Loja(166, 46, player_inventory)
    curses.wrapper(loja.mostrar_loja)

player_inv = {}
iniciar_loja(player_inv)



