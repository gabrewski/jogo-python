import curses
from Interface import shop

def village(window, player, update_inv, update_stats, update_text):
    village_ascii = [
        "                                                                                        ",
        "                                                                                        ",
        "                                 « VILA DO ALVORECER »                                  ",
        "                                                                                        ",
        "                                                                                        ",
        "                                      ________                                          ",
        "                                     /--------\                                 (  )    ",
        "                                    /__________\                                ( )     ",
        "                                   /|          |\                               ()      ",
        "    _______       ________∥___      | []    [] |       ______     ______________∥______ ",
        "   /-------\     /------------\     |          |      /------\     |-----------------|  ",
        "  /_________\   /______________\    |2.Ferraria|     /3.Poção \    |  [ ]  [ ]  [ ]  |  ",
        " /|  ___ [] |\   | []     ___ |     |  ___     |    /|   ___  |\   |  _____          |  ",
        "  |  |`|    |    |1.Forja |´| |     |  |`|     |     |   |´|  |    |  |´  |   [0]    |  ",
        "__|__|_|____|____|________|_|_|_____|__|_|_____|_____|___|_|__|____|__|___|__________|__",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                       M - Mapa                                         "
    ]
    # Limpar tela
    window.clear()
    window.box()

    # Altura e largura da tela
    height, width = window.getmaxyx()

    start_y = (height - len(village_ascii)) // 2
    start_x = (width - len(village_ascii[0])) // 2

    while True:
        window.clear()
        window.box()
        
        for i, line in enumerate(village_ascii):
            window.addstr(start_y + i, start_x, line)
        
        window.refresh()
        
        key = window.getch()

        if key == ord('1'):
            shop.open_weapon_shop(window, player, update_inv)  # Ajuste o player_level conforme necessário
        elif key == ord('2'):
            shop.open_armor_shop(window, player, update_inv)
        elif key == ord('3'):
            shop.open_potion_shop(window, player, update_inv)
        elif key == ord('m') or key == ord('M'):
            return True
        elif key == ord('i'):
            display_inventory(window, player, update_inv, update_stats, update_text)


def display_inventory(window, player, update_inv, update_stats, update_text):
    height, width = window.getmaxyx()

    while True:
        potions = player.inventory.get_consumables()
        equipable = player.inventory.get_equipable()

        itens = potions + equipable
        
        window.clear()
        window.box()

        instructions = "Pressione número para usar ou 'Q' para voltar"

        if not potions and not equipable:
            msg = "Seu inventário está vazio."
            window.addstr(height//2, (width - len(msg))//2, msg)
        
        title = f"Inventário de {player.name}"
        gold_info = f"Seu ouro: {player.inventory.gold}"
        window.addstr(1, (width - len(title))//2, title)
        window.addstr(2, (width - len(gold_info))//2, gold_info)

        start_y = (height - len(itens)) // 4

        for i, item in enumerate(itens):
            item_text = f"{i+1}. {item.name}"
            window.addstr(start_y+i, (width - len(item_text))//2, item_text)

        
        window.addstr(height-2, (width - len(instructions))//2, instructions)
        window.refresh()

        while True:
            key = window.getch()
            if key == ord('q') or key == ord('Q'):
                return
            
            elif key in [ord(str(i+1)) for i in range(len(itens))]:
                item = itens[int(chr(key))-1]

                update_text(pos=(1,2), text='Qual ação deseja realizar?')
                update_text(pos=(2,2), text='[1] Usar       [2] Vender', clear=False)

                while True:
                    opt = window.getch()
                    if opt in [ord('1'), ord('2')]:
                        break

                if hasattr(item, 'hp_value'):
                    if opt == ord('1'):
                        player.heal(item)
                        text = f'{player.name} usou {item.name}'
                        window.addstr(height-3, (width - len(text))//2, text)
                    else:
                        player.inventory.gold += item.gold_value
                        player.inventory.remove_item(item)
                        text = f'{player.name} vendeu {item.name} por {item.gold_value} Gold'
                        window.addstr(height-3, (width - len(text))//2, text)

                elif hasattr(item, 'atk_value'):
                    if opt == ord('1'):
                        player.equip_weapon(item)
                        text = f'{player.name} equipou {item.name}'
                        window.addstr(height-3, (width - len(text))//2, text)
                    else:
                        player.inventory.gold += item.gold_value
                        player.inventory.remove_item(item)
                        text = f'{player.name} vendeu {item.name} por {item.gold_value} Gold'
                        window.addstr(height-3, (width - len(text))//2, text)

                elif hasattr(item, 'def_value'):
                    if opt == ord('1'):
                        player.equip_armor(item)
                        text = f'{player.name} equipou {item.name}'
                        window.addstr(height-3, (width - len(text))//2, text)
                    else:
                        player.inventory.gold += item.gold_value
                        player.inventory.remove_item(item)
                        text = f'{player.name} vendeu {item.name} por {item.gold_value} Gold'
                        window.addstr(height-3, (width - len(text))//2, text)
                    
                update_inv()
                update_stats()
                update_text()
                window.refresh()
                curses.napms(800)
                break
