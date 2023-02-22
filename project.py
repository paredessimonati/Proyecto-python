from room import Room
import attributes

# Create a new instance of the Room class
room = Room()

# Generate a new randomized room
room.new_room()

# Print the description of the current room
print(room.describe_room())
print("\nWhat do you want to do?\nAttack [A] - Run [R] - Investigate room [I]")
if input().strip().lower() == "a":
    print("You attack")
else:
    print("You run")

# print(game_logic.player_hp)
