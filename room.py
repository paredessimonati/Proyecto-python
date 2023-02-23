import random
import attr
import re


class Room:
    def __init__(self) -> None:
        self.current_room = None
        self.description_1 = ""
        self.description_2 = ""
        self.description_3 = ""
        self.description_search = ""
        self.loot = ""
        self.potion = ""
        self.seed = 0

    def enemy_in_room(self):
        return self.current_room

    def room_after_encounter(self):
        return self.description_1, self.description_2, self.description_3

    def room_loot(self):
        return self.loot, self.potion

    def get_attr(self) -> dict:
        # getting all the variables up and randomized
        random_variables_dict = {
            "room": random.choice(attr.room),
            "visibility": random.choice(attr.visibility),
            "temperature": random.choice(attr.temperature),
            "air": random.choice(attr.air),
            "humidity": random.choice(attr.humidity),
            "decoration": random.choice(attr.decoration),
            "furniture": random.choice(attr.furniture),
            "floor texture": random.choice(attr.floor_texture),
            "torch_number": random.choice(attr.torch_number),
            "torches": random.choice(attr.torches),
            "sound": random.choice(attr.sounds),
            "occupancy": random.choice(attr.occupancy),
            "search": random.choice(attr.search),
            "exits": random.sample(attr.exits, random.randrange(1, 4)),
            "trap_doors": random.choice(attr.trap_doors),
            "containers": random.choice(attr.containers),
            "enemy": random.choice(list(attr.enemies)),
            "loot": random.choice(list(attr.loot)),
            "what_in_front": random.choice(attr.what_in_front),
            "directions": random.shuffle(attr.directions),
            "no_enemy": random.choice(attr.no_enemy),
        }

        return random_variables_dict

    def new_room(self):
        if self.current_room is None:
            self.current_room = self.get_attr()
            self.current_room["room"] = "You open your eyes."
        else:
            self.current_room.clear()
            self.current_room = self.get_attr()
        self.seed = str(random.randrange(11111111, 99999999))

    def describe_room(self):
        # setting up long printing variables
        dash_line = "-" * 65
        press_to_continue = f"{'-' * 21}Press Enter to Continue{'-' * 21}"

        # starting to make the string
        # Leaving first line out of the description if the player calls it again.
        print(f'{dash_line}\n\n{self.current_room["room"]}')

        # Starting with empty canvas from line 2.
        for _ in range(1, 5):
            attribute, value = list(self.current_room.items())[_]
            self.description_1 += f"{value}"
        if (
            self.current_room["visibility"] == "room is pitch black. The temperature"
            and self.current_room["torch_number"] == " you see no torches."
        ):
            return (
                self.description_1
            )  # player is effectively blind, need to make special case
        print(self.description_1)

        # Second Line
        self.description_2 = "The decoration is "
        for _ in range(5, 9):
            attribute, value = list(self.current_room.items())[_]
            self.description_2 += f"{value}"
        if self.current_room["torch_number"] != " you see no light sources. ":
            if self.current_room["torch_number"] == " and a few ":
                self.description_2 += (
                    f'{self.current_room["torches"]} torches dimly light the room. '
                )
            elif self.current_room["torch_number"] == " and a single ":
                self.description_2 += (
                    f'{self.current_room["torches"]} torch dimly lights the room. '
                )
            else:
                pass
        print(self.description_2)

        # Third Line
        for _ in range(10, 12):
            attribute, value = list(self.current_room.items())[_]
            self.description_3 += f"{value}"
        input(f"{self.description_3}\n\n{press_to_continue}")

        if self.seed[6:8] > "25":
            self.description = f'{self.current_room["what_in_front"]}'
            self.description += f'{self.current_room["enemy"]}'
            description_enemy = self.description
            print(f"\n{description_enemy}\n")
            input(press_to_continue)
        else:
            self.current_room["enemy"] = "nothing"

    def room_search(self):
        exits = self.current_room["exits"]
        print(f'{self.current_room["search"]}\n')
        print("- Exits:")
        for _ in range(len(exits)):
            print(f"You see {exits[_]} {attr.directions[_]}.")

        if self.seed[0:2] > "95":
            print(f'\nYou see {self.current_room["trap_doors"]} beneath you.')

        if self.seed[2:4] > "00":
            print(
                f'\n- Loot:\nYou see {self.current_room["containers"]} {attr.directions[4]}.'
            )
            self.loot = re.findall(r"'(.*)'", self.current_room["containers"])
        if self.seed[4:6] >= "01":
            self.potion = "red potion"
            print(f"\n- Potion:\nYou see a 'red potion' {attr.directions[5]}.\n")

        return 0
