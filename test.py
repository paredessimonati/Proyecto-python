import random
import attributes

random_variables_dict = {
    "temp": {"value": random.choice(attributes.temperature)},
    "air": {"value": random.choice(attributes.air)},
    "humidity": {"value": random.choice(attributes.humidity)},
    "decoration": {"value": random.choice(attributes.decoration)},
    "furniture": {"value": random.choice(attributes.furniture)},
    "visibility": {"value": random.choice(attributes.visibility)},
    "floor_texture": {"value": random.choice(attributes.floor_texture)},
    "torch": {"value": random.choice(attributes.torches)},
    "sound": {"value": random.choice(attributes.sounds)},
    "exit": {"value": random.choice(attributes.exits)},
    "trap_door": {"value": random.choice(attributes.trap_doors)},
    "container": {"value": random.choice(attributes.containers)},
    "enemy": {"value": random.choice(list(attributes.enemies))},
}

print(random_variables_dict)
