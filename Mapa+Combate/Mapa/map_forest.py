from random import randint
from tile import Tile, plains, forest, pines, mountain, water


class Map:
    def __init__(self, width: int, height: int) -> None: 
        self.width = width
        self.height = height

        self.init_map_data: list[list[str]]
        self.full_map_data: list[[str]]
        self.map_data: list[[str]]
        self.exploration_process: list[list[int]]

        self.generate_map()
        self.generate_patch(forest, 2, 5, 7)
        self.generate_patch(pines, 2, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        self.generate_patch(water, 1, 10, 12)

        self.movement_options = {
            "up": "[W] - UP",
            "down": "[S] - DOWN",
            "left": "[A] - LEFT",
            "right": "[D] - RIGHT"
        }

        self.explored_tiles = [player_marker]

    def load_images(self) -> None:
        for row in self.init_map_data:
            for tile in row:
                tile.load_image()
        
        self.copy_map()

    def generate_map(self) -> None:
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]
        self.copy_map()

    def generate_patch(
            self,
            tile: Tile,
            num_patches: int,
            min_size: int,
            max_size: int,
            irregular: bool = True
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile
        self.copy_map()
    
    def display_movement_options(self, options: dict[str, bool]) -> None:
        for direction, value in self.movement_options.items():
            if options.get(direction):
                print(value)

    def reveal_map(self, pos: list[int]) -> None:
        x, y = pos
        sight_range = range(-2, 3)
        fov = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],

        ]
        for y_index in sight_range:
            tile_y = y + y_index
            if 0 <= tile_y < self.height:
                for x_index in sight_range:
                    tile_x = x + x_index
                    if 0 <= tile_x < self.width and fov[y_index + 2][x_index + 2]:
                        self.exploration_process[tile_y][tile_x] = 1
                        revealed_tile = self.init_map_data[tile_y][tile_x]
                        if revealed_tile not in self.explored_tiles:
                            self.explored_tiles.append(revealed_tile)

    def update_map(self, pos: list[int], marker: Tile) -> None:
        x, y = pos
        self.copy_map()
        self.reveal_map(pos)
        self.map_data[y][x] = marker

    def display_map(self) -> None:
        frame = "x" + self.width * "-" + "x"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)
    
    def copy_map(self) -> None:
        self.map_data = [list(row) for row in self.init_map_data]