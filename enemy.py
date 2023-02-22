import attributes


class Enemy:
    def __init__(self, enemy_in_room):
        self._hp = attributes.enemies[enemy_in_room["enemy"]]["hp"]
        self.attack = int(attributes.enemies[enemy_in_room["enemy"]]["hp"] / 10)
        self.name = enemy_in_room["enemy"][2:]

    @property
    def hp(self):
        return self._hp

    def damage_received(self, n):
        self._hp -= n
