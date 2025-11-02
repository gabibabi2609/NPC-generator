npc_names = input("Name ten different names: ")
names_list = npc_names.split(", ") 


attributes =  [
     "loyal", "brave", "hardworking", "wise", "strong", "clever", "gentle", "humble", "prideful", "proud"
    
]

import random
import time

    
occupations = ["blacksmith", "knight", "jester", "farmer", "cook", "brewer", "weaver", "miller", "fisher", "carpenter", "priest"]
status = ["clergy", "nobility", "lords", "peasantry"]

for name in range(len(names_list)):
    shilling_int = random.randint(99, 999)
    shilling = shilling_int / 10.0
    npc_trait = random.sample(attributes, 3)
    trait1 = npc_trait[0]
    trait2 = npc_trait[1]
    trait3 = npc_trait[2]
    is_able_fight = random.choice([True, False])
    if is_able_fight == True:
        fight_status ="Yes"
    elif is_able_fight == False:
        fight_status = "No"
    print(f"\nCharacter: {random.sample(names_list, k = 1)}\nShillings: {shilling}\nOccupation: {random.choice(occupations)}\nCan they fight? {fight_status}\nTraits: {trait1}, {trait2}, and {trait3}\nSocietal status: {random.choice(status)}")
    print("-----------------------------------------")
    time.sleep(1.0)