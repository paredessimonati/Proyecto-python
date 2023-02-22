from room import Room
from enemy import Enemy
from player import Player
import game_logic
import random

# import game_logic
import attributes


def main():
    # set difficulty
    difficulty = 0

    # Create a new instance of the Room class
    room = Room()

    # Generate a new randomized room
    room.new_room()
    enemy = Enemy(room.enemy_in_room())
    player = Player()
    # Print the description of the current room
    print(room.describe_room())

    # Checking if aggro
    aggro = random.randrange(1, 11) + difficulty
    if aggro <= attributes.enemies[room.current_room["enemy"]]["likelihood"]:
        print(attributes.enemies[room.current_room["enemy"]]["attacks"])
        print()
        game_logic.fight_loop(player, enemy, difficulty)
    else:
        print(attributes.enemies[room.current_room["enemy"]]["no_attack"])
        print()

    game_logic.main_loop(player, room, enemy)
    # if input().strip().lower() == "a":
    #     # print(room.current_room["enemy"])
    #     # print(room.current_room)
    #     print(enemy._hp)
    #     print(player._hp)
    #     # game_logic(room, enemy)
    #     game_logic.game_loop(player, enemy)
    # else:
    #     print("You run")


if __name__ == "__main__":
    main()
