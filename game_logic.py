import random
import attributes


def fight_loop(player, enemy, difficulty):
    new_line = f"\n{'-' * 65}\n\n"
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
                print(f"{new_line}The {enemy.name} lies at your feet.")
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
    while True:
        new_line = f"\n{'-' * 65}\n"
        action = (
            input(
                f"{new_line}\nWhat do you want to do? (Type 'help' for a list of commands):\n\n"
            )
            .strip()
            .lower()
        )
        if action == "help":
            print(
                f"{new_line}Commands: help, room, search, attack, rest, exit\n\nCurrent health: {player._hp}"
            )
        elif action == "room":
            print(new_line)
            for _ in range(3):
                print(f"{room.room_after_encounter()[_]}")
            print(f'\n{attributes.enemies["a " + enemy.name]["after"]}')

        elif action == "search":
            print(new_line)

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
