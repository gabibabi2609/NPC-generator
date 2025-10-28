npc_names = input("\nName ten random names: ")

name_list = npc_names.split(", ")
print(name_list)

npc_list = []
npc_list.append(npc_names)


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
    "evil"
]

import random
import time

for name in range(len(name_list)):
    print(f"\nCharacter: {random.choice(name_list)}")
    print(f"Attributes: {random.choice(attributes)}, {random.choice(attributes)}, {random.choice(attributes)}")


occupations = ["blacksmith", "royal", "knight", "jester", "farmer", "cook"]

for age in range(len(name_list)):
    age_of_character = int(input(f"\nHow old is {random.choice(name_list)}? "))
    if age_of_character >= 7:
        print(f"\nTheir occupation is: {random.choice(occupations)}\n")
    else:
        print("\nThey are too young to work\n")