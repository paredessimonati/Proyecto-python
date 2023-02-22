"""
Attributes
"""
room = [
    "You step through the door and into a new room. The ",
    "The room comes into view as you cross the threshold. The ",
    "You feel a sense of anticipation as you enter the room. The ",
    "The air changes as you step into the new space. The ",
    "The room seems to open up before you as you enter. The ",
    "You take a moment to look around the new space. The ",
    "As you cross the threshold, you sense a change in the air temperature. The ",
    "The room greets you with a sudden shift in atmosphere. The ",
    "You can hear echoes of your footsteps as you step into the room. The ",
    "The space is unfamiliar, but you feel a sense of possibility. The ",
]

visibility = [
    "room is pitch black. The temperature",
    "light is dim. The room ",
    "light is Shadowy. The room ",
    "room is faintly lit. The temperature ",
    "light almost blinds you, the room ",
    "light is blinding, it hurt your eyes. The room ",
    "room is hazy. The temperature ",
    "room is foggy. The temperature ",
    "room is misty. The temperature ",
]

temperature = [
    "is freezing",
    "feels very cold",
    "is cold",
    "feels cool",
    "feels eerily normal",
    "is unremarkable",
    "is surprisingly hot",
    "is alarmingly very hot",
]

air = [
    " and the air feels stale",
    " and the air feels musty",
    " and the air is smoky",
    " and the air is dusty",
    " and the air smells putrid",
    " and the air is fresh",
    " and the air is clean",
    " and the air is aromatic",
    " and the air is floral, you feel like prancing around",
    " and the air is slightly perfumed",
]

humidity = [
    " and dry. ",
    " but slightly humid. ",
    " definitely humid. ",
    " but suffocatingly damp. ",
    " and weirdly moist? ",
    ", the floor is wet. ",
    ", the floor is soaked with something sticky. ",
    ", the walls are soggy. ",
]

decoration = [
    "ornate",
    "plain",
    "minimalistic",
    "cluttered",
    "tasteful",
    "gaudy",
    "elegant",
    "rustic",
    "classic",
    "gothic",
]

furniture = [
    " and the furniture plush.",
    " and the furniture hard.",
    " and the furniture comfortable.",
    " and the furniture uncomfortable.",
    " and the furniture well-made.",
    " and the furniture worn.",
    " and the furniture antique.",
    " and the furniture modern.",
    " and the furniture cheap.",
    " and the furniture expensive.",
    " and the furniture non existent.",
]


floor_texture = [
    " The floor feels rough",
    " The floor feels smooth",
    " The floor feels coarse",
    " The floor feels soft",
    " The floor feels hard",
    " The floor feels legoy",
    " The floor feels crawly",
    " The floor feels fluffy",
    " The floor feels bumpy",
    " The floor feels cold",
]

torch_number = [
    " and a single ",
    " and a few ",
    " and you see no torches.",
]

torches = [
    "black",
    "grey",
    "white",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
]


sounds = [
    "You hear dripping water",
    "You hear creaking floorboards",
    "You hear faint whispers",
    "You hear far away footsteps",
    "You hear wind howling outside",
    "You hear animal noises nearby",
    "You hear chanting monks far away",
    "You hear faint music",
    "You hear shouting far away",
    "You hear silence",
]

occupancy = [
    "The room feels empty. ",
    "The room feels abandoned. ",
    "The room feels quiet. ",
    "The room feels mysterious. ",
    "The room feels haunted. ",
]

exits = [
    "you see a simple door",
    "you see an ornate door",
    "you see a humming door",
    "you see a saloon door",
    "you see a rotten door",
    "you see a metal door",
    "you see a very small door",
    "you see a huge door",
    "you see a velvet curtain",
]

trap_doors = [
    " an out of place carpet.",
    " a trap door.",
]

what_in_front = [
    "Ahead of you lies ",
    "You spot ",
    "Right before you, there is ",
    "Your eyes land on ",
    "In your view is ",
    "Straight ahead is ",
    "Before you is ",
    "You notice ",
    "In front of you appears ",
    "You glimpse ",
]

enemies = {
    "a DRAGON": {
        "likelihood": 9,
        "attacks": "The dragon breathes a blast of fire at you, scorching the \nground beneath your feet!",
        "hp": 100,
        "no_attack": "The dragon sneezes, sending you flying backwards with the \nforce of the blast! It seems uninterested in you.",
    },
    "a cat on a shelf near a glass of water": {
        "likelihood": 5,
        "attacks": "The cat hisses and leaps at you, claws extended!",
        "hp": 10,
        "no_attack": "The cat meows plaintively and stares at a loose thread on \nyour clothing.",
    },
    "a zombie": {
        "likelihood": 7,
        "attacks": "The zombie shambles towards you, arms outstretched and moaning!",
        "hp": 40,
        "no_attack": "The zombie takes one look at you and decides you're not \nworth its time, shuffling off to do something more interesting.",
    },
    "a crying ghost": {
        "likelihood": 5,
        "attacks": "The ghost wails mournfully and flies towards you, phasing through walls and obstacles!",
        "hp": 30,
        "no_attack": "The ghost wails and sobs, bemoaning its own fate and \nleaving you to your own devices.",
    },
    "a sitting gargoyle": {
        "likelihood": 4,
        "attacks": "The gargoyle leaps to its feet and bares its fangs, swooping down to attack you!",
        "hp": 60,
        "no_attack": "For a split second, you think you see the gargoyle move, \nbut upon closer inspection, you realize it's simply a trick of the \nlight. The statue remains motionless, much to your relief.",
    },
    "a pack of rats": {
        "likelihood": 3,
        "attacks": "The rats swarm towards you, biting and clawing!",
        "hp": 20,
        "no_attack": "The rats skitter away at the sound of your approach, \nleaving behind a pile of cheese crumbs.",
    },
    "a giant spider": {
        "likelihood": 7,
        "attacks": "The spider lunges towards you, its fangs dripping with venom!",
        "hp": 50,
        "no_attack": "The spider recoils at the sight of you, looking like it \nhas seen a ghost. It promptly turns and runs away as fast as its \neight spindly legs can carry it, its dignity thoroughly shattered.",
    },
    "a pig": {
        "likelihood": 2,
        "attacks": "The pig charges towards you, its eyes wild with rage!",
        "hp": 30,
        "no_attack": "The pig snorts and grumbles at you, then seems to \nreconsider. 'You're not worth it, kid,' it grunts in a surprisingly \nsophisticated tone. 'Go find someone else to bother.' The pig then \nturns and walks away, leaving you feeling oddly rejected.",
    },
    "a coffer with.. eyes?": {
        "likelihood": 1,
        "attacks": "The coffer suddenly springs open, revealing a set of razor-sharp teeth and a pair of glowing red eyes!",
        "hp": 80,
        "no_attack": "The coffer blinks and blinks again, revealing itself to \nbe a sentient mimic that is happy to chat.",
    },
    "a rabbit with blood dripping from its mouth": {
        "likelihood": 8,
        "attacks": "The rabbit suddenly leaps at you, its teeth bared and its \neyes wild with hunger!",
        "hp": 20,
        "no_attack": "The rabbit hops over to you, looking cute and innocent, \nyou are safe... for now...",
    },
    "a mischievous imp": {
        "likelihood": 10,
        "attacks": "The imp cackles with glee and pelts you with small objects, \nlike stones or bits of garbage!",
        "hp": 50,
        "no_attack": "The imp cackles and performs a small dance for your \namusement, then disappears in a puff of smoke.",
    },
    "a swarm of bees": {
        "likelihood": 2,
        "attacks": "The bees swarm around you, stinging you repeatedly!",
        "hp": 40,
        "no_attack": "The bees buzz around you for a moment, then realize that \nyou're not a flower and fly away.",
    },
    "a wandering ghost with no memory": {
        "likelihood": 7,
        "attacks": "The ghost floats towards you, its eyes clouded and \nunseeing, but its ethereal remarks torment your soul!",
        "hp": 60,
        "no_attack": "The ghost floats past you without noticing you, lost in \nits own thoughts.",
    },
    "a suit of armor": {
        "likelihood": 3,
        "attacks": "The armor suddenly springs to life and attacks you with its sword",
        "hp": 70,
        "no_attack": "The armor simply stands there, silent and inert, like an \nempty suit of armor.",
    },
    "a group of animated garden gnomes": {
        "likelihood": 6,
        "attacks": "The gnomes swarm towards you, attacking you with their \nshovels, watering cans, lamps and pitchforks!",
        "hp": 50,
        "no_attack": "The gnomes stare at you curiously, then go back to their \ngardening tasks.",
    },
    "a shapeshifting slime creature": {
        "likelihood": 4,
        "attacks": "The slime oozes towards you and lashes out with pseudopods, \nattempting to engulf you and absorb you into its body!",
        "hp": 70,
        "no_attack": "The slime creature transforms into a friendly puppy, \nwagging its tail and licking your hand.",
    },
    "a tree": {
        "likelihood": 1,
        "attacks": "The tree suddenly comes to life and attacks you with its branches and roots!",
        "hp": 100,
        "no_attack": "You approach the massive tree. 'Greetings, traveler,' a \ndeep, rumbling voice echoes through your mind. 'Would you care for a \nrefreshing drink and a tale or two?' The tree offers you a cup of \ncool, clear water and settles in to listen to your story.",
    },
    "a grumpy old troll": {
        "likelihood": 8,
        "attacks": "The troll swings its club at you, attempting to knock you \noff and get your boy's soul!",
        "hp": 0,
        "no_attack": "The troll is too busy playing night crawlers to notice \nyou.",
    },
    "a scarecrow": {
        "likelihood": 3,
        "attacks": "The scarecrow suddenly springs to life, wielding a \npitchfork and murderous eyes!",
        "hp": 0,
        "no_attack": "The scarecrow comes to life, waving a friendly greeting \nas you approach. 'Hello there!' it chirps. 'Is there anything I can \ndo to help you?' It then settles back into its post and doesnt move \nagain",
    },
    "a flock of magical fire-breathing chickens": {
        "likelihood": 9,
        "attacks": "The chickens flutter towards you, belching flames and \nscorching the ground!",
        "hp": 0,
        "no_attack": "The chickens cluck and peck at the ground, one of them \nroasts an unlucky worm",
    },
    "a floating sword": {
        "likelihood": 5,
        "attacks": "The sword suddenly lunges towards you, attempting to slash \nyou!",
        "hp": 0,
        "no_attack": "The sword simply hovers in the air, waiting for a worthy wielder to claim it.",
    },
}

containers = [
    "large cracked metal safe",
    "sturdy wooden chest with iron hardware",
    "ornate marble urn with a removable lid",
    "steel tool cabinet with multiple drawers",
    "weathered stone well with a bucket and rope",
    "tall armoire with double doors and a key",
    "heavy metal locker with a padlock",
    "painted wooden wardrobe with shelves and a lock",
    "large leather-bound trunk with metal corners and handles",
    "a plain chest",
]


treasure = {
    "JEWEL_NECKLACE": {
        "value": 70,
        "description": "A stunning necklace adorned with glittering jewels.",
    },
    "GOLD_BROOCH": {
        "value": 80,
        "description": "A beautiful brooch inlaid with precious gems.",
    },
    "SILVER_CANDELABRUM": {
        "value": 60,
        "description": "An ornate candelabrum made of polished silver.",
    },
    "ANCIENT_SCROLL": {
        "value": 90,
        "description": "A weathered scroll containing ancient magical incantations.",
    },
    "VELVET_SPICE_POUCH": {
        "value": 50,
        "description": "A soft velvet pouch filled with rare and valuable spices.",
    },
    "LEATHER_TOME": {
        "value": 60,
        "description": "A leather-bound tome filled with secret knowledge.",
    },
    "IVORY_FIGURINE": {
        "value": 75,
        "description": "A delicately carved ivory figurine of a mythical creature.",
    },
    "TREASURE_MAP": {
        "value": 35,
        "description": "A map leading to a hidden treasure trove.",
    },
    "SILVER_HAND_MIRROR": {
        "value": 55,
        "description": "A delicate hand mirror made of polished silver.",
    },
    "HAIR_LOCKET": {
        "value": 20,
        "description": "A locket containing a lock of hair from a long-dead lover.",
    },
    "POTION_INVISIBILITY": {
        "value": 90,
        "description": "A vial containing a potion of invisibility.",
    },
    "BEJEWELED_GOBLET": {
        "value": 70,
        "description": "A bejeweled goblet fit for a king.",
    },
    "GOLD_COINS": {
        "value": 300,
        "description": "A chest full of rare gold coins.",
    },
    "SILVER_SCEPTER": {
        "value": 85,
        "description": "A silver scepter with a crystal orb at its tip.",
    },
    "ENCHANTED_BOOTS": {
        "value": 95,
        "description": "A pair of boots that grant the wearer great speed.",
    },
    "MAGICAL_LANTERN": {
        "value": 60,
        "description": "A lantern that illuminates even the darkest corners with magical light.",
    },
    "ENCHANTED_ARMOR": {
        "value": 75,
        "description": "A suit of armor with protective enchantments.",
    },
    "MYSTERIOUS_ORB": {
        "value": 90,
        "description": "A mysterious orb that hums with magical energy.",
    },
    "GIANT_DIAMOND": {
        "value": 1000,
        "description": "A gleaming diamond the size of a fist.",
    },
    "ANCIENT_RELIQUARY": {
        "value": 150,
        "description": "An ornate reliquary containing the preserved remains of a saint or hero.",
    },
}
