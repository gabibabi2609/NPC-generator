npc_names = input("Name ten random names: ")

npc_list = []
npc_list.append(npc_names)

# print(npc_list)

attributes =  [
    "bloodstained",
    "faceless",
    "rotting",
    "whispering",
    "cursed",
    "shadowy",
    "twisted",
    "decayed",
    "haunting",
    "ashen",
    "glowing",
    "stitched",
    "banshee",
    "possessed",
    "soulless",
    "skeletal",
    "mutated",
    "phantom",
    "tattered",
    "gory",
    "grim",
    "lurking",
    "eldritch",
    "hollow",
    "ominous",
    "distorted",
    "ravenous",
    "bleeding",
    "burned",
    "pale",
    "sinister",
    "crimson",
    "silent",
    "vile",
    "cold",
    "deranged",
    "tormented",
    "infected",
    "unholy",
    "macabre"
]

import random 
print(random.choice(npc_names), random.choice(attributes), random.choice(attributes), random.choice(attributes), random.choice(attributes))