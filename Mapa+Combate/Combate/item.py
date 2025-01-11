class Item:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value

potion = Item(name = "Poção de Cura", value = 10)