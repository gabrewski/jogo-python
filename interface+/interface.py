import curses

# fazer os imports aqui
# importar os coisos do jogador (nome e level) do sistema de progresso
# importar o mapa
# importar os itens do sistema de inventário
# importar o combate

class GameInterface:
    def __init__(self, stdscr):
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
        CYAN = curses.color_pair(2)
        GREEN = curses.color_pair(3)
        MAGENTA = curses.color_pair(4)
        RED = curses.color_pair(5)
        WHITE = curses.color_pair(6)
        YELLOW = curses.color_pair(7)
        
        self.setup_windows()
        self.refresh_all()
        
    def setup_windows(self):
        self.max_y, self.max_x = self.stdscr.getmaxyx()
        
        # Área principal do jogo (70% da largura)
        game_width = int(self.max_x * 0.7)
        game_height = self.max_y - 5  # Altura total menos área de comandos
        self.game_win = curses.newwin(game_height, game_width, 0, 0)
        
        # Largura dos painéis laterais
        side_width = self.max_x - game_width
        
        # Informações do personagem (nome, level e HP)
        self.char_win = curses.newwin(5, side_width, 0, game_width)
        
        # Status do personagem
        self.stats_win = curses.newwin(8, side_width, 5, game_width)
        
        # Inventário
        inv_height = self.max_y - 13 
        self.inv_win = curses.newwin(inv_height, side_width, 13, game_width)
        
        # Área de comandos
        self.cmd_win = curses.newwin(5, game_width, game_height, 0)
        
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
    
    def update_game_area(self, game_map=None):
        """Atualiza a área principal do jogo"""
        self.game_win.clear()
        self.game_win.box()
        
        # usar seu módulo de mapa
        # if (mapa):
        #     for y, row in enumerate(mapa.tiles):
        #         for x, tile in enumerate(row):
        #             self.game_win.addch(y + 1, x + 1, tile.char)
        
        # Por enquanto, apenas um exemplo
        self.game_win.addstr(1, 1, "@ - Player")
        self.game_win.refresh()
    
    def update_character(self, name="Hero", level=1, hp=100, max_hp=100):
        """Atualiza informações do personagem"""
        self.char_win.clear()
        self.char_win.box()
        self.char_win.addstr(1, 2, f"Name: {name}")
        self.char_win.addstr(2, 2, f"Level: {level}")
        self.char_win.addstr(3, 2, f"HP: {hp}/{max_hp}")
        self.char_win.refresh()
    
    def update_stats(self, stats=None):
        """Atualiza status do personagem"""
        self.stats_win.clear()
        self.stats_win.box()
        
        # if stats:
        #     display_stats = [
        #         f"STR: {stats.strength}",
        #         f"DEX: {stats.dexterity}"
        #     ]
        
        # Por enquanto, valores de exemplo, não sei o que vai ter
        stats = [
            "MP: ████████── 80/100",
            "STR: 15",
            "DEX: 12",
            "INT: 10",
            "DEF: 8"
        ]
        for i, stat in enumerate(stats, 1):
            self.stats_win.addstr(i, 2, stat)
        self.stats_win.refresh()
    
    def update_inventory(self, inventory=None):
        """Atualiza o inventário"""
        self.inv_win.clear()
        self.inv_win.box()
        self.inv_win.addstr(1, 2, "Inventory:")
        
        # if inventory:
        #     items = inventory.get_items()
        
        # Por enquanto, itens de exemplo
        items = ["Health Potion", "Iron Sword", "Leather Armor", "Magic Ring"]
        for i, item in enumerate(items, 2):
            self.inv_win.addstr(i, 2, f"- {item}")
        self.inv_win.refresh()
    
    def update_commands(self):
        """Atualiza a área de comandos"""
        self.cmd_win.clear()
        self.cmd_win.box()
        commands = [
            "   W          ↑                   |        Q - Quit             |        P - Pause ",
            "                    - Move        |                             |                  ",
            "A  S  D    ←  ↓  →                |        I - Inventory        |        M - Map   "
            ]
        for i, command in enumerate(commands, 1):
            self.cmd_win.addstr(i, 2, command)
            
        self.cmd_win.refresh()

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
    
    # Dá inicializar outros módulos
    # player = Player("Hero", 1)
    # world = World()
    # game_map = generate_map(80, 24)
    # inventory = Inventory()
    
    # Atualiza todas as áreas
    interface.update_game_area()
    interface.update_character()
    interface.update_stats()
    interface.update_inventory()
    interface.update_commands()
    
    # Loop principal
    while True:
        try:
            key = stdscr.getch()
            
            if key == ord('q'):
                break
            
            # Como interagir com outros módulos (pensando sobre aquele código que eu tinha feito antes)
            # if key in [ord('w'), ord('s'), ord('a'), ord('d')]:
            #     player.move(key)
            #     world.update()
            #     interface.update_game_area(world.get_current_map())
            #     interface.update_character(player.name, player.level, player.hp)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except curses.error as e:
        print(f"Erro ao inicializar curses: {e}")

# Não faço a menor ideia de como ligar todas as coisas :D
# Hoje farei a parte da loja que ficou comigo 