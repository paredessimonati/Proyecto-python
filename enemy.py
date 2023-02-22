import random
import attributes
from room import Room

room = Room()
description = room.describe_room()


class Enemy:
    def __init__(self):
        current_room = Room.describe_room()
        self._hp = int(attributes.enemies[current_room["enemy"]]["hp"])
        self.attack = int(attributes.enemies[current_room["enemy"]]["hp"]) / 2
        self.name = attributes.enemies[current_room["enemy"]]

    @property
    def hp(self):
        return self._hp

    def damage_received(self, n):
        self._hp -= n
