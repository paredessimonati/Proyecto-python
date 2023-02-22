import random
import attributes


class Room:
    def __init__(self) -> None:
        self.current_room = None
        self.description_1 = ""
        self.description_2 = ""
        self.description_3 = ""

    def enemy_in_room(self):
        return self.current_room

    def room_after_encounter(self):
        return self.description_1, self.description_2, self.description_3

    def get_attributes(self) -> dict:
        # getting all the variables up and randomized
        random_variables_dict = {
            "room": random.choice(attributes.room),
            "visibility": random.choice(attributes.visibility),
            "temperature": random.choice(attributes.temperature),
            "air": random.choice(attributes.air),
            "humidity": random.choice(attributes.humidity),
            "decoration": random.choice(attributes.decoration),
            "furniture": random.choice(attributes.furniture),
            "floor texture": random.choice(attributes.floor_texture),
            "torch_number": random.choice(attributes.torch_number),
            "torches": random.choice(attributes.torches),
            "sound": random.choice(attributes.sounds),
            "occupancy": random.choice(attributes.occupancy),
            "exits": random.choice(attributes.exits),
            "trap_doors": random.choice(attributes.trap_doors),
            "container": random.choice(attributes.containers),
            "enemy": random.choice(list(attributes.enemies)),
            "treasure": random.choice(list(attributes.treasure)),
            "what_in_front": random.choice(attributes.what_in_front),
            "search": random.choice(attributes.search),
        }

        # some variables wont happen every time, separating for easier adjustment
        # random_number = random.randrange(1, 10)
        if random.randrange(1, 10) < 3:
            random_variables_dict["trap_door"] = 0
        if random.randrange(1, 10) < 4:
            random_variables_dict["treasure"] = 0
        return random_variables_dict

    def new_room(self):
        if self.current_room == None:
            self.current_room = self.get_attributes()
            self.current_room["room"] = "You open your eyes."
        else:
            self.current_room = self.get_attributes()

    def describe_room(self):
        # setting up long printing variables
        dash_line = "-" * 65
        press_to_continue = f"{'-' * 21}Press Enter to Continue{'-' * 21}"

        # starting to make the string
        # Leaving first line out of the description if the player calls it again.
        print(f'{dash_line}\n\n{self.current_room["room"]}')

        # Starting with empty canvas from line 2.
        for _ in range(1, 5):
            attr, value = list(self.current_room.items())[_]
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
            attr, value = list(self.current_room.items())[_]
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
            attr, value = list(self.current_room.items())[_]
            self.description_3 = f"{value}"
        # description += f"{random.choice(['To the left ', 'To the right '])}"
        # description += f'{self.current_room["exits"]}'
        # if random.randrange(100) < 30:
        #     description += f'you see {self.current_room["trap_doors"]}'

        # Last line before enemy, asking for input to continue
        print(f"{self.description_3}\n\n{press_to_continue}")
        input()

        self.description = f'{self.current_room["what_in_front"]}'
        self.description += f'{self.current_room["enemy"]}'
        description_enemy = self.description
        print(f"{description_enemy}\n")
        print(press_to_continue)
        return input()
    
    def search_room(self)
        return
