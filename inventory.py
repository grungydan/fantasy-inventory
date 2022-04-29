#!/usr/bin/env python3
import copy

'''
This is an implementation of the inventory carried by a character in a fantasy game. 
Project modified slightly from Automate the Boring Stuff, Sweigart

Original project spec called for new items to be added merely via string recognition, whereas 
this version takes new items in as a dictionary and adds them to the inventory without list conversion.

While writing this version, I discovered and utilized the copy module of Python3
'''

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


def add_to_inventory(newItems):
    '''If item exists in inventory, add item.value to quantity. If item is new, add item as new k,v pair.'''
    # create a shallow copy of newItems dict
    ghostItems = copy.copy(newItems)
    print(ghostItems)
    for key in newItems: 
        if key in inventory.keys():
            print(f"You have {key} already, so you add more to your inventory.")
            inventory[key] = inventory[key] + ghostItems[key]
            ghostItems.pop(key)
            print(inventory[key])
            print(ghostItems)
        else: 
            pass
            
            

#displayInventory()

add_to_inventory({'rope' : 1, 'dragon toenails': 4})