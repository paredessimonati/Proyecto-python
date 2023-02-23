from room import Room
from enemy import Enemy
from player import Player
import game_logic
import random

# import game_logic
import attr


def main():
    # set difficulty
    difficulty = 0

    # Create a new instance of the Room class

    player = Player()
    # Generate a new randomized room

    while player._hp > 0:
        room = Room()
        room.new_room()
        enemy = Enemy(room.enemy_in_room())

        # Print the description of the current room
        room.describe_room()

        # Checking if enemy appeared
        if room.current_room["enemy"] == "nothing":
            game_logic.main_loop(player, room, enemy, difficulty)
        else:
            # Checking if aggro
            aggro = random.randrange(1, 11) + difficulty
            if aggro <= attr.enemies[room.current_room["enemy"]]["likelihood"]:
                print(f'\n{attr.enemies[room.current_room["enemy"]]["attacks"]}')
                input(f"\n{'-' * 21}Press Enter to Continue{'-' * 21}")
                game_logic.fight_loop(player, enemy, difficulty)
            else:
                print(f'\n{attr.enemies[room.current_room["enemy"]]["no_attack"]}')
                print()
        game_logic.main_loop(player, room, enemy, difficulty)

        continue


if __name__ == "__main__":
    main()
