#!/usr/bin/env python3
import copy

inventory = {'rope': 3, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory():
    '''Display the current inventory'''
    print("Your inventory currently contains the following: ")
    for key, value in inventory.items():
        print(f"{key}, {value}")
    numItems = 0
    for item in inventory.items():
        numItems += 1
    print(f"Total number of different items in your inventory: {numItems}")


def addToInventory(foundItems):
    '''If item exists in inventory, add item.value to quantity. If item is new, add item as new k,v pair.'''
    # create a shallow copy of newItems dict
    ghostItems = copy.copy(foundItems)
    print(ghostItems.__sizeof__())
    for key in foundItems: 
        if key in inventory.keys():
            print(f"You have {key} already, but you could always use more, so you add it to your pack.")
            inventory[key] = inventory[key] + ghostItems[key]
            del ghostItems[key]
            # print("new stuff",ghostItems)
        
        elif key not in inventory.keys():
            newItems = {key:ghostItems[key]}
            print(f"You did not have any {key}, so you add it to your pack.")
            inventory.update(newItems.items())
            del ghostItems[key]
                
        
            
        

displayInventory()  
print("*" * 20)
addToInventory({'rope': 1, 'dragon toenails': 3, 'potion of healing': 5, 'arrow': 3 })
print("*" * 20)
displayInventory()