import random
import attr
import sys


def fight_loop(player, enemy, difficulty):
    new_line = f"{'-' * 27}Health: {player._hp}{'-' * 27}\n"
    press_to_continue = f"{'-' * 21}Press Enter to Continue{'-' * 21}\n"
    while True:
        # Combat loop
        while player.hp > 0 and enemy.hp > 0:
            # Player attacks enemy
            player_attack = player.attack + random.randrange(-5, 5)
            enemy_attack = enemy.attack + random.randrange(-3, 5) + (difficulty * 2)
            if round(random.random(), 2) < 0.15:
                print(f"You missed the {enemy.name}!")
            else:
                print(f"You attack the {enemy.name} for {player_attack} damage!")
                enemy._hp -= player_attack
            # Check if enemy is still alive
            if enemy._hp <= 0:
                print(f'{attr.enemies[enemy.name]["defeat"]}\n')
                enemy.alive = 0
                break

            # Enemy attacks player
            if round(random.random(), 2) < 0.2:
                print(f"The {enemy.name} misses you!\n")
            else:
                print(f"The {enemy.name} attacks you for {enemy_attack} damage!\n")
                player._hp -= enemy_attack

            # Check if player is still alive
            if player._hp <= 0:
                print(f"{'-' * 21}You died{'-' * 21}")
                break

            input(press_to_continue)
        break


def main_loop(player, room, enemy, difficulty):
    search_status = 0
    if room.current_room["enemy"] == "nothing":
        enemy_present = 0
    else:
        enemy_present = 1
    while True:
        new_line = f"{'-' * 27}Health: {player._hp}{'-' * 27}\n"
        action = (
            input(
                f"{new_line}\nWhat do you want to do?\nCommands: Room, Search, Attack, Open, Drink, Exit\n\nType command: "
            )
            .strip()
            .lower()
        )
        # elif action[0] == "help":
        #     print(f"\nCommands: help, room, search, attack, open, drink, exit\n")

        if action == "room" or action == "r":
            print(new_line)
            for _ in range(3):
                print(f"{room.room_after_encounter()[_]}")
            if enemy_present == 1 and enemy.alive == 0:
                print(f'\n{attr.enemies[enemy.name]["after"]}')
            else:
                print(f'\n{room.current_room["no_enemy"]}')

        elif action == "search" or action == "s":
            print(new_line)
            room.room_search()
            search_status = 1
            continue

        elif action == "open" or action == "o":
            loot_item = attr.loot[room.current_room["loot"]]["description"]
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
                    print(f"Do you want to open the {loot[0]}?\n")
                    loot_choice = input(f"Yes - No\n").strip().lower()
                    if loot_choice == "y" or loot_choice == "yes":
                        print(f"You receive {loot_item}\n")
                        # receive a buff maybe?
                        ...
                        room.seed = room.seed[:2] + "00" + room.seed[4:]
                    elif loot_choice == "n" or loot_choice == "no":
                        print("Ok, better safe than sorry.\n")
                    else:
                        raise ValueError("Invalid Input")
                    break
                except ValueError:
                    search_status += 1
                    if search_status == 15:
                        sys.exit("come on....")
                    pass

            continue

        elif action == "drink" or action == "d":
            if search_status == 0:
                print("\nYou need to search the room first.")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                continue
            try:
                loot, potion = room.room_loot()
            except IndexError:
                print("You didnt find anything, try the next room.\n")
                break
            if potion == "":
                input("\nYou didnt find anything, try the next room.\n")
                continue
            while True:
                try:
                    print("Do you want to drink the potion?\n")
                    pot = input(f"Yes - No\n").strip().lower()
                    if pot == "y" or pot == "yes":
                        print("You feel refreshed\n")
                        player.damage_received(-100)
                        room.seed = room.seed[:4] + "00" + room.seed[6:]
                    elif pot == "n" or pot == "no":
                        print("Ok, better safe than sorry.\n")
                    else:
                        raise ValueError("Invalid Input")
                    break
                except ValueError:
                    search_status += 1
                    if search_status == 15:
                        sys.exit("come on....")
                    pass

            continue

        elif action == "attack" or action == "a":
            if enemy_present == 1 and enemy.alive == 1:
                print(f"Are you sure you want to attack a {enemy.name}?")
                attack = input(f"Yes - No\n").strip().lower()
                if attack == "y" or attack == "yes":
                    fight_loop(player, enemy, difficulty)
            else:
                print("\nThere's nothing to attack.")
        elif action == "exit" or action == "e":
            if search_status == 0:
                print("\nYou need to search the room first.")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
                continue
            exits = room.current_room["exits"]
            print("\nChoose carefully.")
            for _ in range(len(exits)):
                print(f"{_ + 1} - {exits[_]}")
            if input("\nType door number: ") != "":
                print(new_line)
                return
            else:
                continue

    # else:
    #     print("Invalid command. Type 'help' for a list of commands.")
