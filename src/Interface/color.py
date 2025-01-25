# color.py
import curses

class ColorManager:
    _instance = None
    _colors_initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def init_colors(self):
        if not self._colors_initialized:
            curses.start_color()
            curses.use_default_colors()
            self._init_tile_colors()
            self._init_ui_colors()
            self._colors_initialized = True

    def _init_tile_colors(self):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)   
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)    
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)     
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)   
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)    
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)   

    def _init_ui_colors(self):
        curses.init_pair(16, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(17, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(18, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(19, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(20, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(21, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(22, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    def tile_colors(self):
        return {
            'YELLOW': curses.color_pair(1),
            'GREEN': curses.color_pair(2),
            'LIGHT_GREEN': curses.color_pair(3),
            'BLUE': curses.color_pair(4),
            'LIGHT_BLUE': curses.color_pair(5),
            'RED': curses.color_pair(6),
            'LIGHT_RED': curses.color_pair(7),
            'WHITE': curses.color_pair(8),
            'MAGENTA': curses.color_pair(9),
            'CYAN': curses.color_pair(10),
            'LIGHT_GRAY': curses.color_pair(11),
            'DARK_GRAY': curses.color_pair(12),
            'BROWN': curses.color_pair(13),
            'MAGMA': curses.color_pair(14),
            'LIGHT_CYAN': curses.color_pair(15),
        }

    def ui_colors(self):
        return {
            'BLUE': curses.color_pair(16),
            'CYAN': curses.color_pair(17),
            'GREEN': curses.color_pair(18),
            'MAGENTA': curses.color_pair(19),
            'RED': curses.color_pair(20),
            'WHITE': curses.color_pair(21),
            'YELLOW': curses.color_pair(22),
        }


COLOR = ColorManager()