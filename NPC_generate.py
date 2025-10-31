npc_names = input("Name ten different names: ")
names_list = npc_names.split(", ") 


attributes =  [
     "loyal", "brave", "hardworking", "wise", "strong", "clever", "gentle", "humble", "prideful", "proud"
    
]

import random
import time

    
occupations = ["blacksmith", "royal", "knight", "jester", "farmer", "cook"]



for name in range(len(names_list)):
    age_of_character = int(input(f"\nHow old is {random.choice(names_list)}? "))
    shilling_int = random.randint(100, 600)
    shilling = shilling_int / 100.0
    attributes = random.sample(attributes, k = 3)
    print(attributes)
    attribute1 = attributes[0]
    attribute2 = attributes[1]
    attribute3 = attributes[2]
    is_able_fight = random.choice([True, False])
    if is_able_fight == True:
        fight_status ="Yes"
    elif is_able_fight == False:
        fight_status = "No"

print(f"Character: {random.sample(names_list)}\nOccupation: {random.choice(occupations)}\nCan they fight? {fight_status}\nTraits: {attribute1}, {attribute2}, and {attribute3}")
print("----------------------------------")