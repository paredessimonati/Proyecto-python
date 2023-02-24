from game_logic_new import main_loop
from player import Player
import text
import os

DEBUG_MODE = 1  # skips intro and stuff


def main():
    # Set difficulty (damage received)
    difficulty = 0

    # Set probability of the enemy spawning in the current room.
    enemy_spawning = 99

    if DEBUG_MODE == 0:
        # clear the screen
        os.system("cls")
        print(text.castle)
        text.title2("ADVENTURE!!!")
        # Create a Player
        player = Player()
        player_name = input("Please enter your name:")
    else:
        player = Player()
    os.system("cls")
    # player.name = input(...TODO...)

    # add some story

    # Start the game
    # Counter for how many rooms the player cleared.
    room_counter = 0
    game_variables = {
        "difficulty": difficulty,
        "enemy_spawning": enemy_spawning,
        "player": player,
        "room_counter": room_counter,
    }
    main_loop(game_variables)

    # # debug section

    # print("------")
    # print("------")
    # print("------")
    # print("------")
    # print("------")
    # print("------")
    # print(room_counter)


if __name__ == "__main__":
    main()
