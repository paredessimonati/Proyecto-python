import attr
import os
import sys
import text
from enemy import Enemy
from room import Room


def main_loop(var):
    # unpacking variables
    difficulty, enemy_spawning, player, room_counter = var.values()
    while player.hp > 0:
        # Create a room

        room = Room()
        room.new_room()
        seed = room.seed

        # Room enemy
        # Even though an enemy instance is created for every room
        # i dont want an enemy in every single one, 90% of the time i do.
        enemy = Enemy(room.current_room)
        enemy_name = enemy.name
        enemy.is_visible(seed, enemy_spawning)
        enemy_spawn = enemy.visible

        ...

        # Room description
        description = room.describe_room(room_counter, enemy_spawn)
        text.format(description, "jump")
        text.super_line()
        input()
        # Describe enemy if visible
        os.system("cls")
        description = ""
        if enemy.visible is True:
            description = enemy.description(seed, difficulty, room)

            # If enemy is aggro, automatic fight
            if enemy.aggro is True:
                description += attr.enemies[enemy_name]["attacks"]
                text.format(description, "double")
                text.super_line()
            else:
                description += attr.enemies[enemy_name]["no_attack"]
                text.format(description, "double")
                text.super_line()

        # enemy.description(seed, difficulty, room)
        # print(seed)
        # print(player.hp)
        # print("enemy_name")
        # print(enemy_name)
        # print("enemy")
        # print(enemy.visible)
        # print("room")
        # print(room.current_room["what_in_front"])
        # print(room_counter)
        # print(text.line)
        # x = room.describe_room(1, True)
        # text.format(x)
        sys.exit()
        return room_counter  # DONT FORGET
