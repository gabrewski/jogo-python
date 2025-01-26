#main.py

import curses
from Interface.map_module import show_map
from Combat.combat_test import CombatSystem
from Combat.combat_interface import start_combat
from Mapa.main import Exploration

# fazer os imports aqui
# Importar os coisos do jogador (nome e level) do sistema de progresso
# Importar os coiso de mapa aleatório
# Importar os itens do sistema de inventário
# Importar o combate

class GameInterface:
    def __init__(self, stdscr, player):
        self.player = player

        self.stdscr = stdscr
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        
        # configuração de cores
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) 
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)  
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK) 
        curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
        curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_BLACK)  
        curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_BLACK)
        
        self.setup_windows()
        self.refresh_all()
        
    # DESENHANDO OS QUADRADINHOS E PAH
    def setup_windows(self):
        self.max_y, self.max_x = self.stdscr.getmaxyx()
        
        # Área principal do jogo (70% da largura)
        self.game_width = int(self.max_x * 0.75)
        self.game_height = self.max_y - 7  # Altura total menos área de comandos
        self.game_win = curses.newwin(self.game_height, self.game_width, 0, 0)
        
        # Largura dos painéis laterais
        side_width = self.max_x - self.game_width
        
        # Informações do personagem (nome, level e HP)
        self.char_win = curses.newwin(5, side_width, 0, self.game_width)
        
        # Status do personagem
        self.stats_win = curses.newwin(6, side_width, 5, self.game_width)
        
        # Inventário (área vertical menos os comandos)
        inv_height = self.max_y - 18
        self.inv_win = curses.newwin(inv_height, side_width, 11, self.game_width)

        # Área de comandos
        cmd_y = self.max_y - 7
        self.cmd_win = curses.newwin(7, side_width, cmd_y, self.game_width)

        # Área de narração (mesma largura da área do jogo)
        self.txt_win = curses.newwin(7, self.game_width, self.game_height, 0)
        
        self.draw_borders()
    
    def draw_borders(self):
        for win in [self.game_win, self.char_win, self.stats_win, self.inv_win, self.txt_win]:
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
    def update_game_area(self, game_map=[]):
        """Atualiza a área principal do jogo"""
        self.game_win.clear()
        self.game_win.box()

        for i, row in enumerate(game_map):
            col_count = 1

            for tile in row:
                if tile == " ":
                    self.game_win.addstr(i+1, col_count, "  ")
                else:
                    self.game_win.addstr(i+1, col_count, tile.symbol, curses.color_pair(tile.color_pair))
                col_count += 1

        self.game_win.refresh()

    def update_character(self):
        """Atualiza informações do personagem"""
        self.char_win.clear()
        self.char_win.box()
        self.char_win.addstr(1, 2, f"Name: {self.player.name}")
        self.char_win.addstr(2, 2, f"Level: {self.player.level}")
        self.char_win.addstr(3, 2, f"HP: {self.player.hp}/{self.player.hp_max}")
        self.char_win.refresh()

    #mudei essa parte //// gabi    
    def update_stats(self, stats=None):
        """Atualiza status do personagem"""
        self.stats_win.clear()
        self.stats_win.box()
        
        #obtem os stats do personagem
        player_stats = self.player.get_stats()
        
        #valores dinâmicos pra barrinha
        exp_bar = int((player_stats["exp"] / player_stats["exp_to_next_level"]) * 10)   #barrinha de xp com 10 blocos
        exp_display = f"EXP: {'█' * exp_bar}{'─' * (10 - exp_bar)} {player_stats['exp']}/{player_stats['exp_to_next_level']}"
        
        #stats do personagem
        stats = [
            exp_display,
            f"HP: {player_stats['hp']}",
            f"ATK: {player_stats['atk']}",
            f"DEF: {player_stats['defense']}",
        ]
        
        #isso atualiza o negocio mas tem que testar ainda
        for i, stat in enumerate(stats, 1):
            self.stats_win.addstr(i, 2, stat)
        self.stats_win.refresh()

    # ~~~~ fim da mudança ~~~~
    
    def update_inventory(self):
        """Atualiza o inventário"""
        self.inv_win.clear()
        self.inv_win.box()
        self.inv_win.addstr(1, 2, "Inventory:")
        
        # Por enquanto, itens de exemplo, tem que pegar do inventario
        items = self.player.inventory.player_items
        
        for i, item in enumerate(items, 2):
            self.inv_win.addstr(i, 2, f"- {item}")
        self.inv_win.refresh()
    
    def update_commands(self):
        """Atualiza a área de comandos"""
        self.cmd_win.clear()
        self.cmd_win.box()
        commands = [
            "        W          | Q - Sair     ",
            "     A  S  D       | I - Inventario",
            "                   | M - Mapa      ",
            "      Move         | ↲ - Confirmar  "
            ]
        for i, command in enumerate(commands, 1):
            self.cmd_win.addstr(i, 2, command)
            
        self.cmd_win.refresh()

    def update_text(self, pos=(1,1), text=None, clear:bool = True):
        """Atualiza a área de narração"""
        if clear:
            self.txt_win.clear()
            self.txt_win.box()

        if pos and text:
            self.txt_win.addstr(*pos, text)
        self.txt_win.refresh()

    # COISAS ACONTECENDO 
    def show_world_map(self):
        """Mostra o mapa do mundo na área principal do jogo"""
        selected_area = show_map(self.game_win)
        self.game_win.refresh()
        return selected_area

def start_interface(stdscr, player):  
    curses.curs_set(0)
    stdscr.clear()
    
    interface = GameInterface(stdscr, player)
    exploration = Exploration((interface.game_width-3, interface.game_height-2))
    combat_system = CombatSystem(interface.game_win,
                                 interface.txt_win, 
                                 interface.update_text, 
                                 interface.update_character,
                                 interface.update_stats)
    
    
    interface.update_game_area()
    interface.update_character()
    interface.update_stats()
    interface.update_inventory()
    interface.update_commands()
    interface.update_text()
    
    
    while True:
        key = stdscr.getch()
        
        if key in [ord('q'), 27]:  
            break
        elif key in [ord('m'), ord('M')]:  
            selected_area = interface.show_world_map()
            
            stage_mapping = {
                1: 1,  # Montanha
                2: 1,  # Floresta
                3: 2,  # Deserto
                4: 3,  # Neve
                5: 4,  # Pântano
                6: 5   # Magma
            }
            
            if selected_area not in stage_mapping:
                continue
        
            while True:

                if exploration.map_loop(player, 
                                        stage_mapping[selected_area], 
                                        interface.update_game_area,
                                        stdscr):
                    enemy = combat_system.get_random_enemy(stage_mapping[selected_area])

                    if not combat_system.start_combat(player, enemy):
                        break
                else:
                    break
                

            interface.update_game_area([])
            interface.update_character()
            interface.update_stats()
            interface.update_inventory()
            interface.update_commands()
            interface.update_text()
