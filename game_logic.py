import random
import attributes
import sys


def fight_loop(player, enemy, difficulty):
    new_line = f"{'-' * 27}Health: {player._hp}{'-' * 27}\n"
    press_to_continue = f"{'-' * 21}Press Enter to Continue{'-' * 21}\n"
    while True:
        # Combat loop
        while player.hp > 0 and enemy.hp > 0:
            # Player attacks enemy
            player_attack = player.attack + random.randrange(-3, 3)
            enemy_attack = enemy.attack + random.randrange(-3, 3) + (difficulty * 2)
            enemy._hp -= player_attack
            print(f"You attack the {enemy.name} for {player_attack} damage!")

            # Check if enemy is still alive
            if enemy._hp <= 0:
                print(f'{attributes.enemies[enemy.name]["defeat"]}\n')
                break

            # Enemy attacks player
            player._hp -= enemy_attack
            print(f"The {enemy.name} attacks you for {enemy_attack} damage!\n")

            # Check if player is still alive
            if player._hp <= 0:
                print(f"{'-' * 21}You died{'-' * 21}")
                break

            input(press_to_continue)
        break


def main_loop(player, room, enemy):
    search_status = 0
    while True:
        new_line = f"{'-' * 27}Health: {player._hp}{'-' * 27}\n"
        commands = [
            "help",
            "room",
            "search",
            "attack",
            "open",
            "drink",
            "exit",
        ]
        action = (
            input(
                f"{new_line}\nWhat do you want to do?\nCommands: Room, Search, Attack, Open, Drink, exit\n\nType command: "
            )
            .strip()
            .lower()
        )
        if action not in commands:
            print("\nWrong command.")

        # elif action[0] == "help":
        #     print(f"\nCommands: help, room, search, attack, open, drink, exit\n")

        elif action == "room":
            print(new_line)
            for _ in range(3):
                print(f"{room.room_after_encounter()[_]}")
            print(f'\n{attributes.enemies[enemy.name]["after"]}')

        elif action == "search":
            print(new_line)
            room.room_search()
            search_status = 1

        elif action == "open":
            if search_status == 0:
                print("\nYou need to search the room first.")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                continue
            try:
                loot, potion = room.room_loot()
            except IndexError:
                print("You didnt find anything, try the next room.\n")
                break
            if loot == "":
                input("\nYou didnt find anything, try the next room.\n")
                continue
            while True:
                try:
                    print("What item do you wish to open?\n")
                    lootz = input(f"1 - {loot[0]}\n\n")
                    if lootz != "1" and lootz != loot[0]:
                        raise ValueError("Invalid Input")
                    break
                except ValueError:
                    search_status += 1
                    if search_status == 15:
                        sys.exit("come on....")
                    pass
            lootz = attributes.treasure[room.current_room["treasure"]]["description"]

            print(f"\n\nYou found {lootz}\n\n")
            attributes.treasure[room.current_room["treasure"]][
                "description"
            ] = "looks empty."
            continue

        #     print(current_room.describe_room())
        # elif action == "move":
        #     current_room.new_room()
        #     print(current_room.describe_room())
        # elif action == "attack":
        #     if "enemy" not in current_room.current_room():
        #         print("There is no enemy here to attack!")
        #     else:
        #         # Start combat loop
        #         pass
        # elif action == "exit":
        #     return
        # else:
        #     print("Invalid command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    game_loop()
