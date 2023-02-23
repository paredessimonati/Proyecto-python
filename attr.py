"""
Attributes
"""
room = [
    "You step through the door and into a new room.",
    "The room comes into view as you cross the threshold.",
    "You feel a sense of anticipation as you enter the room.",
    "The air changes as you step into the new space.",
    "The room seems to open up before you as you enter.",
    "You take a moment to look around the new space.",
    "As you cross the threshold, you sense a change in the air temperature.",
    "The room greets you with a sudden shift in atmosphere.",
    "You can hear echoes of your footsteps as you step into the room.",
    "The space is unfamiliar, but you feel a sense of possibility.",
]

visibility = [
    "The room is pitch black. The temperature",
    "The light is dim. The room ",
    "The light is Shadowy. The room ",
    "The room is faintly lit. The temperature ",
    "The light almost blinds you, the room ",
    "The light is blinding, it hurts your eyes. The room ",
    "The room is hazy. The temperature ",
    "The room is foggy. The temperature ",
    "The room is misty. The temperature ",
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
    " and the air feels aromatic",
    " and the air smells like flowers",
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
]


floor_texture = [
    " The floor feels rough",
    " The floor feels smooth",
    " The floor feels coarse",
    " The floor feels soft",
    " The floor feels hard",
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
    "You hear dripping water. ",
    "You hear creaking floorboards. ",
    "You hear faint whispers. ",
    "You hear far away footsteps. ",
    "You hear wind howling outside. ",
    "You hear animal noises nearby. ",
    "You hear chanting monks far away. ",
    "You hear faint music. ",
    "You hear shouting far away. ",
    "You hear silence. ",
]

occupancy = [
    "The room feels empty. ",
    "The room feels abandoned. ",
    "The room feels oddly familiar. ",
    "The room feels mysterious. ",
    "The room feels haunted. ",
]

exits = [
    "a 'simple door'",
    "an 'ornate door'",
    "a 'strange door'",
    "a 'broken door'",
    "a 'rotten door'",
    "a 'very small door'",
    "a 'huge door'",
    "a 'velvet curtain'",
    "a 'wooden door'",
    "a 'glass door'",
    "a 'stone door'",
    "a 'metal door'",
    "a 'steel door'",
    "a 'double door'",
    "a 'sliding door'",
    "a 'screen door'",
    "a 'vault door'",
]

directions = [
    "to the left",
    "to the right",
    "up ahead",
    "far off",
    "in the distance",
    "over there",
    "pretty near",
    "a short distance away",
    "not to far away",
    "within sight",
    "a few steps away",
    "just up ahead",
    "behind a pile of garbage",
    "behind a pile of bones",
    "near a pile of garbage",
    "near a pile of bones",
    "near the rests of a campfire",
    "near a fireplace",
    "near a bookshelf",
    "at the back of the room",
    "hidden in the shadows",
]

trap_doors = [
    "a trap door",
]

what_in_front = [
    "Ahead of you lies a ",
    "You spot a ",
    "Right before you, there is a ",
    "Your eyes land on a ",
    "In your view is a ",
    "Straight ahead is a ",
    "Before you is a ",
    "You notice a ",
    "In front of you appears a ",
    "You glimpse a ",
]

no_enemy = [
    "a chill runs down your spine",
    "Your palms start to sweat.",
    "You feel a tightness in your chest.",
    "The hairs on the back of your neck stand up.",
    "You feel a sense of impending doom.",
    "Your mind races with uncertainty.",
    "Your knees begin to buckle.   ",
    "You feel like you're being watched.",
    "Your eyes dart around nervously.   ",
    "You are filled with a sense of emptiness.",
]

search = [
    "You look around the room...",
    "You examine the area...",
    "You take a walk around the room...",
    "You investigate the surroundings...",
    "You explore the room...",
    "You take a quick glance around...  ",
    "You search for anything useful...",
    "You check for anything out of place...",
    "You look for any hidden objects...",
    "Surely there must be something here...",
]

enemies = {
    "DRAGON": {
        "likelihood": 9,
        "attacks": "The dragon breathes a blast of fire at you, scorching the \nground beneath your feet!",
        "hp": 100,
        "defeat": "The dragon lets out a deafening roar before falling to the \nground.",
        "after": "The carcass of a dragon lies at your feet.",
        "no_attack": "The dragon sneezes, sending you flying backwards with the \nforce of the blast! It seems uninterested in you.",
    },
    "cat on a shelf near a glass of water": {
        "likelihood": 5,
        "attacks": "The cat hisses and leaps at you, claws extended!",
        "hp": 12,
        "defeat": "The cat hisses before running off to safety.",
        "after": "The cat is nowhere to be seen.",
        "no_attack": "The cat meows plaintively and stares at a loose thread on \nyour clothing.",
    },
    "zombie": {
        "likelihood": 7,
        "attacks": "The zombie moves towards you, arms outstretched and \nmoaning!",
        "hp": 40,
        "defeat": "The zombie groans and collapses into a pile of putrid meat.",
        "after": "You take a few steps back, the smell is nauseating.",
        "no_attack": "The zombie takes one look at you and decides you're not \nworth its time, shuffling off to do something more interesting.",
    },
    "crying ghost": {
        "likelihood": 5,
        "attacks": "The ghost wails angrily and flies towards you, phasing \nthrough walls and obstacles! It attacks!",
        "hp": 30,
        "defeat": "The crying ghost lets out a last wail before disappearing \ninto the ether.",
        "after": "A chill runs down your spine...",
        "no_attack": "The ghost wails and sobs, bemoaning its own fate and \nleaving you to your own devices.",
    },
    "sitting gargoyle": {
        "likelihood": 4,
        "attacks": "The gargoyle leaps to its feet and bares its fangs, \nswooping down to attack you!",
        "hp": 60,
        "defeat": "The gargoyle makes a horrible noise before breaking into \npieces.",
        "after": "You kick the gargoyle head away.",
        "no_attack": "For a split second, you think you see the gargoyle move, \nbut upon closer inspection, you realize it's simply a trick of the \nlight. The statue remains motionless, much to your relief.",
    },
    "pack of rats": {
        "likelihood": 3,
        "attacks": "The rats swarm towards you, biting and clawing!",
        "hp": 20,
        "defeat": "The rats squeak and scatter in all directions.",
        "after": "A few stale bread crumbs lie at your feet.",
        "no_attack": "The rats skitter away at the sound of your approach, \nleaving behind a pile of stale bread crumbs.",
    },
    "giant spider": {
        "likelihood": 7,
        "attacks": "The spider lunges towards you, its fangs dripping with \nvenom!",
        "hp": 50,
        "defeat": "The giant spider screeches before showering the ground with a putrid mixture of green goo and spiderlings...",
        "after": "A big spider lies in front with its legs curled up and green \ngoo keeps pouring from it.",
        "no_attack": "The spider recoils at the sight of you, looking like it \nhas seen a ghost. It promptly turns and runs away as fast as its \neight spindly legs can carry it, its dignity thoroughly shattered.",
    },
    "pig": {
        "likelihood": 2,
        "attacks": "The pig charges towards you, its eyes wild with rage!",
        "hp": 30,
        "defeat": "The pig lets out a pitiful oink before running away",
        "after": "The pig is hiding behind behind a curtain.",
        "no_attack": "The pig snorts and grumbles at you, then seems to \nreconsider. 'You're not worth it, kid,' it grunts in a surprisingly \nsophisticated tone. 'Go find someone else to bother.' The pig then \nturns and walks away, leaving you feeling oddly rejected.",
    },
    "coffer with.. eyes?": {
        "likelihood": 1,
        "attacks": "The coffer suddenly springs open, revealing a set of \nrazor-sharp teeth and a pair of glowing red eyes!",
        "hp": 80,
        "defeat": "The mimic makes a sophisticated and theatrical scream \nbefore revealing all its contents",
        "after": "The mimic's treasure is right in front of you.",
        "no_attack": "The coffer blinks and blinks again, revealing itself to \nbe a sentient mimic that is happy to chat.",
    },
    "rabbit with blood dripping from its mouth": {
        "likelihood": 8,
        "attacks": "The rabbit suddenly leaps at you, its teeth bared and its \neyes wild with hunger!",
        "hp": 20,
        "defeat": "The rabbit jumps away to safety.",
        "after": "The rabbit looks at you at a distance.",
        "no_attack": "The rabbit hops over to you, looking cute and innocent, \nyou are safe... for now...",
    },
    "mischievous imp": {
        "likelihood": 10,
        "attacks": "The imp cackles with glee and pelts you with small stones \nand bits of garbage!",
        "hp": 50,
        "defeat": "The imp cackles maniacally as it fades away.",
        "after": "You wish you could fade away like the imp sometimes.",
        "no_attack": "The imp cackles and performs a small dance for your \namusement, then disappears in a puff of smoke.",
    },
    "swarm of bees": {
        "likelihood": 2,
        "attacks": "The bees swarm around you, stinging you repeatedly!",
        "hp": 40,
        "defeat": "The swarm of bees buzzes angrily before flying off, you \nswear one of them gave you the bird.",
        "after": "You search for the beehive, but find nothing.",
        "no_attack": "The bees buzz around you for a moment, then realize that \nyou're not a flower and fly away.",
    },
    "wandering ghost with no memory": {
        "likelihood": 7,
        "attacks": "The ghost floats towards you, its eyes clouded and \nunseeing, but its ethereal remarks torment your soul!",
        "hp": 60,
        "defeat": "The wandering ghost hurts you one more time and fades away \ninto the mist without looking back.",
        "after": "The wandering ghost is just but a memory now.",
        "no_attack": "The ghost floats past you without noticing you, lost in \nits own thoughts.",
    },
    "suit of armor": {
        "likelihood": 3,
        "attacks": "The armor suddenly springs to life and attacks you with its sword",
        "hp": 70,
        "defeat": "The suit of armor clatters to the ground, silent once more.",
        "after": "You try the suit on, it's way too big.",
        "no_attack": "The armor simply stands there, silent and inert, like an \nempty suit of armor.",
    },
    "group of animated garden gnomes": {
        "likelihood": 6,
        "attacks": "The gnomes swarm towards you, attacking you with their \nshovels, watering cans, lamps and pitchforks!",
        "hp": 50,
        "defeat": "The gnomes grunt and groan as they become inanimate once \nagain.",
        "after": "You know you've always hated these things.",
        "no_attack": "The gnomes stare at you curiously, then go back to their \ngardening tasks.",
    },
    "shapeshifting slime creature": {
        "likelihood": 4,
        "attacks": "The slime oozes towards you and lashes out with pseudopods, \nattempting to engulf you and absorb you into its body!",
        "hp": 70,
        "defeat": "The shapeshifting slime lets out a wet gurgle before \ndissolving into a puddle.",
        "after": "You try not to step into the puddle...",
        "no_attack": "The slime creature transforms into a friendly puppy, \nwagging its tail and licking your hand.",
    },
    "tree": {
        "likelihood": 1,
        "attacks": "The tree suddenly comes to life and attacks you with its branches and roots!",
        "hp": 100,
        "defeat": "The tree rustles its leaves and offers a deep, sad sigh.",
        "after": "You look at the tree, any sign of consciousness is now gone.",
        "no_attack": "You approach the massive tree. 'Greetings, traveler' a \ndeep, rumbling voice echoes through your mind. 'Would you care for a \nrefreshing drink and a tale or two?' The tree offers you a cup of \ncool, clear water and settles in to listen to your story.",
    },
    "grumpy old troll": {
        "likelihood": 8,
        "attacks": "The troll swings its club at you, attempting to knock you \noff and get your boy's soul!",
        "hp": 60,
        "defeat": "The grumpy old troll cries as the Dayman comes and takes it \naway",
        "after": "You feel like you're in some elaborate play...",
        "no_attack": "The troll is too busy playing night crawlers to notice \nyou.",
    },
    "scarecrow": {
        "likelihood": 3,
        "attacks": "The scarecrow suddenly springs to life, wielding a \npitchfork and murderous eyes!",
        "hp": 40,
        "defeat": "The scarecrow makes a rustling sound before going limp.",
        "after": "A crow now rests on top of it, you have no idea where it came \nfrom",
        "no_attack": "The scarecrow comes to life, waving a friendly greeting \nas you approach. 'Hello there!' it chirps. 'Is there anything I can \ndo to help you?' It then settles back into its post and doesnt move \nagain",
    },
    "flock of magical fire-breathing chickens": {
        "likelihood": 9,
        "attacks": "The chickens flutter towards you, belching flames and \nscorching the ground!",
        "hp": 60,
        "defeat": "The fire-breathing chickens let out a cacophony of clucks \nand squawks as they run away bursting into flames.",
        "after": "The chickens are now scattered piles of ash.",
        "no_attack": "The chickens cluck and peck at the ground, one of them \nroasts an unlucky worm",
    },
    "floating sword": {
        "likelihood": 5,
        "attacks": "The sword suddenly lunges, its attempting to slash you!",
        "hp": 40,
        "defeat": "The floating sword falls to the ground.",
        "after": "You crouch to take the sword but there's nothing there.",
        "no_attack": "The sword simply hovers in the air, waiting for a worthy \nwielder to claim it.",
    },
}

containers = [
    "large cracked 'metal safe'",
    "sturdy 'wooden chest' with iron hardware",
    "very ornate 'marble urn' with a removable lid",
    "steel 'tool cabinet' with multiple drawers",
    "weathered 'stone well' with a bucket and rope",
    "tall 'armoire' with double doors and a key",
    "heavy 'metal locker' with a padlock",
    "wooden 'wardrobe' with shelves and cabinets",
    "large leather-bound 'trunk' with metal corners and handles",
    "'plain chest'",
    "'chest'",
]


loot = {
    "JEWEL_NECKLACE": {
        "value": 70,
        "description": "a stunning necklace adorned with glittering jewels.",
    },
    "GOLD_BROOCH": {
        "value": 80,
        "description": "a beautiful brooch inlaid with precious gems.",
    },
    "SILVER_CANDELABRUM": {
        "value": 60,
        "description": "an ornate candelabrum made of polished silver.",
    },
    "ANCIENT_SCROLL": {
        "value": 90,
        "description": "a weathered scroll containing ancient magical incantations.",
    },
    "VELVET_SPICE_POUCH": {
        "value": 50,
        "description": "a soft velvet pouch filled with rare and valuable spices.",
    },
    "LEATHER_TOME": {
        "value": 60,
        "description": "a leather-bound tome filled with secret knowledge.",
    },
    "IVORY_FIGURINE": {
        "value": 75,
        "description": "a delicately carved ivory figurine of a mythical creature.",
    },
    "TREASURE_MAP": {
        "value": 35,
        "description": "a map leading to a hidden treasure trove.",
    },
    "SILVER_HAND_MIRROR": {
        "value": 55,
        "description": "a delicate hand mirror made of polished silver.",
    },
    "HAIR_LOCKET": {
        "value": 20,
        "description": "a locket containing a lock of hair from a long-dead lover.",
    },
    "POTION_INVISIBILITY": {
        "value": 90,
        "description": "a vial containing a potion of invisibility.",
    },
    "BEJEWELED_GOBLET": {
        "value": 70,
        "description": "a bejeweled goblet fit for a king.",
    },
    "GOLD_COINS": {
        "value": 300,
        "description": "a chest full of rare gold coins.",
    },
    "SILVER_SCEPTER": {
        "value": 85,
        "description": "a silver scepter with a crystal orb at its tip.",
    },
    "ENCHANTED_BOOTS": {
        "value": 95,
        "description": "a pair of boots that grant the wearer great speed.",
    },
    "MAGICAL_LANTERN": {
        "value": 60,
        "description": "a lantern that illuminates even the darkest corners with magical light.",
    },
    "ENCHANTED_ARMOR": {
        "value": 75,
        "description": "a suit of armor with protective enchantments.",
    },
    "MYSTERIOUS_ORB": {
        "value": 90,
        "description": "a mysterious orb that hums with magical energy.",
    },
    "GIANT_DIAMOND": {
        "value": 1000,
        "description": "a gleaming diamond the size of a fist.",
    },
    "ANCIENT_RELIQUARY": {
        "value": 150,
        "description": "an ornate reliquary containing the preserved remains of a saint or hero.",
    },
}
