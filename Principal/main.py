import curses
from map_module import show_map
from character import Player
from save_load import SaveLoadSystem 
from inventario import Inventario, Item

# fazer os imports aqui
# Importar os coisos do jogador (nome e level) do sistema de progresso
# Importar os coiso de mapa aleatório
# Importar os itens do sistema de inventário
# Importar o combate

class GameInterface:
    def __init__(self, stdscr):
        # Inicializa o sistema de progressão
        self.stdscr = stdscr
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        
        # configuração de cores
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        BLUE = curses.color_pair(1)
        self.setup_windows()
        self.refresh_all()
        
    # DESENHANDO OS QUADRADINHOS E PAH
    def setup_windows(self):
        self.max_y, self.max_x = self.stdscr.getmaxyx()
        
        # Área principal do jogo (70% da largura)
        game_width = int(self.max_x * 0.75)
        game_height = self.max_y - 7  # Altura total menos área de comandos
        self.game_win = curses.newwin(game_height, game_width, 0, 0)
        
        # Largura dos painéis laterais
        side_width = self.max_x - game_width
        
        # Informações do personagem (nome, level e HP)
        self.char_win = curses.newwin(5, side_width, 0, game_width)
        
        # Status do personagem
        self.stats_win = curses.newwin(6, side_width, 5, game_width)
        
        # Inventário (área vertical menos os comandos)
        inv_height = self.max_y - 18
        self.inv_win = curses.newwin(inv_height, side_width, 11, game_width)

        # Área de comandos
        self.cmd_win = curses.newwin(7, side_width, 34, game_width)

        # Área de narração (mesma largura da área do jogo)
        self.txt_win = curses.newwin(7, game_width, game_height, 0)
        
        self.draw_borders()
    
    def draw_borders(self):
        for win in [self.game_win, self.char_win, self.stats_win, self.inv_win, self.cmd_win]:
            win.box()
    
    def refresh_all(self):
        self.stdscr.refresh()
        self.game_win.refresh()
        self.char_win.refresh()
        self.stats_win.refresh()
        self.inv_win.refresh()
        self.cmd_win.refresh()
        self.txt_win.refresh()
    
    #ATUALIZAÇÕES DE INFORMAÇÕES
    def update_game_area(self, game_map=None):
        """Atualiza a área principal do jogo"""
        self.game_win.clear()
        self.game_win.box()

        # Por enquanto, apenas um exemplo
        self.game_win.addstr(2, 3, "começa na vila")
        self.game_win.refresh()
    def update_character(self, name="Hero", level=1, hp=100, max_hp=100):
        """Atualiza informações do personagem"""
        self.char_win.clear()
        self.char_win.box()
        self.char_win.addstr(1, 2, f"Name: {name}")
        self.char_win.addstr(2, 2, f"Level: {level}")
        self.char_win.addstr(3, 2, f"HP: {hp}/{max_hp}")
        self.char_win.refresh()

    #mudei essa parte //// gabi    
    def update_stats(self, player):
        """Atualiza status do personagem"""
        self.stats_win.clear()
        self.stats_win.box()
        
        # valores dinâmicos para a barra de experiência
        exp_bar = int((player.exp / player.level_exp[player.level]) * 10)  # barra de xp com 10 blocos
        exp_display = f"EXP: {'█' * exp_bar}{'─' * (10 - exp_bar)} {player.exp}/{player.level_exp[player.level]}"
        
        # stats do personagem
        stats = [
            exp_display,
            f"HP: {player.hp}/{player.hp_max}",
            f"ATK: {player.atk + player.weapon.atk_value if player.weapon else player.atk}",
            f"DEF: {player.armor.def_value if player.armor else 0}",
            f"Crit Chance: {player.crit_chance * 100:.1f}%",
            f"Crit Damage: {player.crit_damage}x"
        ]
        
        # atualiza a janela de status
        for i, stat in enumerate(stats, 1):
            self.stats_win.addstr(i, 2, stat)
        self.stats_win.refresh()

    # ~~~~ fim da mudança ~~~~
    
    def update_inventory(self, inventory):
        """Atualiza o inventário"""
        self.inv_win.clear()
        self.inv_win.box()
        self.inv_win.addstr(1, 2, "Inventory:")
        
        # Por enquanto, itens de exemplo, tem que pegar do inventario
        items = ["Health Potion", "Iron Sword", "Leather Armor", "Magic Ring"]
        
        for i, item in enumerate(items, 2):
            self.inv_win.addstr(i, 2, f"- {item}")
        self.inv_win.refresh()
    
    def update_commands(self):
        """Atualiza a área de comandos"""
        self.cmd_win.clear()
        self.cmd_win.box()
        commands = [
            "    W         ↑    | P - Pause    ",
            "                   | Q - Quit     ",
            " A  S  D   ←  ↓  → | I - Inventory",
            "                   | M - Map      ",
            "       Move        | ↲ - Confirm  "
            ]
        for i, command in enumerate(commands, 1):
            self.cmd_win.addstr(i, 2, command)
            
        self.cmd_win.refresh()

    def update_text(self):
        """Atualiza a área de narração"""
        self.txt_win.clear()
        self.txt_win.box()

        # Por enquanto, apenas um exemplo
        self.txt_win.addstr(1, 1, "Narração")
        self.txt_win.refresh()        

    # COISAS ACONTECENDO 
    def show_world_map(self):
        """Mostra o mapa do mundo na área principal do jogo"""
        result = show_map(self.game_win)
        selected_area = result  # Adjust this based on the actual return values of show_map
        self.game_win.refresh()
        return selected_area

def main(stdscr):
    # Verifica tamanho mínimo do terminal
    height, width = stdscr.getmaxyx()
    if height < 24 or width < 80:
        stdscr.addstr(0, 0, "Terminal muito pequeno! Precisa ser pelo menos 80x24")
        stdscr.refresh()
        stdscr.getch()
        return
    
    stdscr.clear()
    stdscr.refresh()
    
    # Inicializa a interface
    interface = GameInterface(stdscr)
       
    # inicializar os outros módulos? talvez fique tudo igual eu coloquei o mapa
    # player = Player("Hero", 1)
    # world = World()
    # inventory = Inventory()
    # sei lá, algo assim
    
    # Inicializa o jogador
    player = Player("Hero", 1, 10, 0.1, 1.5)
    
    # Atualiza todas as áreas
    interface.update_game_area()
    interface.update_character()
    interface.update_stats(player)
    inventory = Inventario(slots=15, gold=0, player_items=[
        Item(name="Health Potion", gold_value=10, equipable=False, consumable=True, tradable=True),
        Item(name="Iron Sword", gold_value=50, equipable=True, consumable=False, tradable=True),
        Item(name="Leather Armor", gold_value=30, equipable=True, consumable=False, tradable=True),
        Item(name="Magic Ring", gold_value=100, equipable=True, consumable=False, tradable=True)
    ])
    interface.update_inventory(inventory)
    interface.update_commands()
    interface.update_text()
    
    # Loop principal

    while True:
        try:
            key = stdscr.getch()
            player = Player("Hero", 1, 10, 0.1, 1.5)
            interface.update_stats(player)
            if key == ord('q'):
                # salva o jogo e sai
                save_load_system = SaveLoadSystem("savefile.txt")
                save_load_system.save_game(player, inventory)
                break
            elif key == ord('m') or key == ord('M'):
                selected_area = interface.show_world_map()

                #talvez tenha que mudar pq vão ter outras partes que vão ser com número, tipo o menu principal ou o combate, veremos
                if selected_area == 1:
                    #carregar montanha
                    interface.update_game_area()

                elif selected_area == 2:
                    # Carregar floresta
                    interface.update_game_area()

                elif selected_area == 3:
                    # Carregar planícies
                    interface.update_game_area()

                elif selected_area == 4:
                    # Carregar água
                    interface.update_game_area()

                elif selected_area == 5:
                    # carregar deserto
                    interface.update_game_area()

                elif selected_area == 6:
                    # carregar magma
                    interface.update_game_area()

                else:  # selected_area == 7 ou inválido
                    interface.update_game_area()

        except KeyboardInterrupt:
            break
        except Exception as e:
            stdscr.addstr(0, 0, f"Erro: {e}")
            stdscr.refresh()
            stdscr.getch()
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"Erro: {e}")
        curses.endwin()


