import random
import attributes
import player


class Room:
    def __init__(self) -> None:
        self.current_room = None

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
            self.current_room["room"] = "You open your eyes. The "
        else:
            self.current_room = self.get_attributes()

    def describe_room(self):
        description = ""

        # starting to make the string
        # First line
        for _ in range(5):
            attr, value = list(self.current_room.items())[_]
            description += f"{value}"
        if (
            self.current_room["visibility"] == "room is pitch black. The temperature"
            and self.current_room["torch_number"] == " you see no torches."
        ):
            return description  # player is effectively blind, need to make special case
        print(description)

        # Second Line
        description = "The decoration is "
        for _ in range(5, 9):
            attr, value = list(self.current_room.items())[_]
            description += f"{value}"
        if self.current_room["torch_number"] != " you see no torches. ":
            if self.current_room["torch_number"] == " and a few ":
                description += f'{self.current_room["torches"]} torches. '
            elif self.current_room["torch_number"] == " and a single ":
                description += f'{self.current_room["torches"]} torch. '
            else:
                pass
        print(description)

        # Third Line
        for _ in range(10, 12):
            attr, value = list(self.current_room.items())[_]
            description = f"{value}"
        description += f"{random.choice(['To the left ', 'To the right '])}"
        description += f'{self.current_room["exits"]}'
        if random.randrange(100) < 30:
            description += f'you see {self.current_room["trap_doors"]}'
        description_room_only = description

        # Last line before enemy, asking for input to continue
        print(f"{description_room_only}\nPress Enter to Continue..")
        input()
        print("---------------------------------------------------------------------")
        description = f'{self.current_room["what_in_front"]}'
        description += f'{self.current_room["enemy"]}'
        description_enemy = description
        print(f"{description_enemy}")
        print("---------------------------------------------------------------------")
        # Checking if aggro
        aggro = random.randrange(10) + 1
        if aggro <= attributes.enemies[self.current_room["enemy"]]["likelihood"]:
            return attributes.enemies[self.current_room["enemy"]]["attacks"]
        else:
            return attributes.enemies[self.current_room["enemy"]]["no_attack"]
