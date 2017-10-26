#!/usr/bin/python3


##### NEED TO DO:
##### clean up text
##### graphics
##### win condition
##### death handling

from playergame import *
from itemsgame_OO import *
from itemsgame import * 
from gameparser import *
import random
from mapgame import rooms
from enemies import *
from enemies_OO import *
from questions_OO import *

global debugMode
debugMode = False

# Use this to print debug strings, so that we can easily toggle on/off the debug outputs.
def printDebug(string):
    if(debugMode):
        print(string)

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    newlist = ""
    for item in items:
        newlist = newlist + (item.sName) + ", "
    newlist = newlist.rstrip()[:-1]
    return newlist

def list_of_enemies(enemies):
    newList = ""
    for enemy in enemies:
        newList += enemy.sName + ", "
    newList = newList.rstrip()[:-1]
    return newList
    
def list_of_items_quantities(items):
    newList = ""
    i = 0
    for item in items:
        if(i>0):
            newList += ", "
        newList += (str(item.iQuantity) + " " + item.sName)
        i+=1
    return newList

def print_room_items(room):
    if list_of_items(room["items"]) != "":
        print("There is " + (list_of_items(room["items"]) + " here.\n"))

def print_inventory_items(items):
    print("You have " + list_of_items_quantities(items) + ".\n")

def print_enemy_room(room):
    newList = []
    for enemy in room["enemies"]:
        if enemy.bAlive:
            newList.append(enemy)
    
    if len(newList) > 1:
        print((list_of_enemies(newList) + " are here!\n"))
    elif len(newList) == 1:
        print((list_of_enemies(newList) + " is here!\n"))

def print_room(room):
    # Display room name
    
    for i in range(0, 10):
        print("\n")
    
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    print_enemy_room(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        if item.sName == "Printer":
            print("PRINT BOOK to spend 1 print credit and print off a book.")
            print("PRINT THESIS to spend 5 print credits and print off Kirill's thesis.")
        else:
            print("TAKE " + item.sName.upper() + " to take " + item.sName + ".")


    for enemy in player.current_room["enemies"]:
        print("FIGHT " + enemy.sName.upper() + " to battle " + enemy.sName if enemy.bAlive else "" )

    print("USE <item> to use an item.")
    print("DROP <item> to drop an item.")

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    if direction in player.current_room["exits"]:
        player.current_room = move(player.current_room["exits"], direction)
        print_room(player.current_room)
    else:
        print("You cannot go there")

def buy_book(itemToBuy):
    #global total_mass
    
    if(itemToBuy.lower() == "thesis"):
        itemToBuy = Thesis()
    elif(itemToBuy.lower() == "book"):
        itemToBuy = Textbook()
    else:
        print("That's not a printable item.")
        return
    
    # If the player has print credits
    # Python wizardry: isInstance will tell you if x is an instance of A
    # any() will determine if any of the items in the provided list are an instance of A
    #
    # Best method for finding an item in the inventory is next(item for item in player.inventory if isinstance(item, OBJECT_TYPE)) 
    #
    
    #if( any(isinstance(item, Printcred) for item in player.inventory) ):
    for item in player.inventory:
        if type(item) == Printcred:
            print("Printing", item.iQuantity, itemToBuy.sName, "for", itemToBuy.iCost, "printer credits.")
            # If the player can fit the item in the inventory and they've got enough credits
            #print(itemToBuy.iCost)
            #print(item.iQuantity)
            
            if itemToBuy.fMass + player.updateMass() < player.maxMass and item.iQuantity >= itemToBuy.iCost:#player.inventory[player.inventory.index(Printcred())].iQuantity >= itemToBuy.iCost:
                if(any(isinstance(item, type(itemToBuy)) for item in player.inventory)):
                    next(item for item in player.inventory if isinstance(item, type(itemToBuy))).iQuantity += 1
                else:
                    player.inventory.append(itemToBuy)
                                
                item.iQuantity -= itemToBuy.iCost
                if item.iQuantity <= 0:
                    player.inventory.remove(next(item for item in player.inventory if isinstance(item, Printcred)))
                
                player.checkOverEncumbered()            
        #else:
        #    print("You can't take this item as you carry to many items, or don't have enough print credits.")

def execute_take(item_id):
    for item in player.current_room["items"]:
        if (item.sName.upper() in item_id.upper()):
            if(item in player.inventory):
                next(x for x in player.inventory if isinstance(x, type(item))).iQuantity += 1
            else:
                #player.inventory.append(item)
                item.add(player)
            print("You add the item to your inventory.")
            player.updateMass()    
            player.current_room["items"].remove(item)
            return
            #else:
            #    print("You can't take this item as you carry too much weight. You must drop items.")
            #    print("Mass: " + str(player.updateMass()) + ", Maximum Mass: " + str(player.maxMass))
            #    return 
    print("You cannot take that.")
    return 

def execute_drop(item_id):
    for item in player.inventory:
        if item.sName.upper() in item_id.upper() and not item.sName.upper() == "HANDBOOK":
            player.current_room["items"].append(item)
            #player.inventory.remove(item)
            item.deplete(player)
            player.updateMass()
            return

    print("You cannot drop that.")
    
def execute_useitem(item_id):
    for item in player.inventory:
        
        if item.sName.upper() in item_id.upper() and item.bUsable:
            # This is why OO programming is absolutely superior for games
            # Instead of case-selecting the item type, I can simply call the function 'useItem',
            # which, being defined for the superclass GenericItem, can be called from any item,
            # regardless of which subclass it is, because they all inherit (and some override)
            # the function.
            
            item.useItem(player)
            
            if item.bFinite:
                item.deplete(player)
            return    
        
    # If a return statement is never hit:        
    print("You don't have that item.")

def execute_fight_command(command, enemy):
    # Return false if the command was nonsensical or incorrect.
    # If the command was successful, return true

    if 0 == len(command):
        return False

    if command[0].upper() == "ATTACK":
        if len(command) > 1:
            execute_attack(command[1], enemy)
            return True
        else:
            print("Attack with what? Use 'ATTACK HANDS' to slap the enemy!")
            print_inventory_items(player.inventory)
            return False
            
    elif command[0].upper() == "USE":
        if len(command) > 1:    
            execute_useitem(command[1])
            return True
        else:
            print("Use what?")
            print_inventory_items(player.inventory)
            return False
    elif command[0].upper() == "LEAVE":
            execute_leave()
            return True
    else:
        print("That makes no sense.")
        return False

def fight_loop(enemy_id): #TODO: UPDATE THIS TO OO
    for enemy in player.current_room["enemies"]:
        if enemy.sName.upper() in enemy_id.upper():

            print(enemy.sDesc, end="\n\n")
            
            while enemy.bAlive and player.isAlive:
                print_inventory_items(player.inventory)
                print("Enemy health: " + str(enemy.iHealth) + "/" + str(enemy.iMaxHealth))
                print("You can:\nATTACK with an item\nUSE an item\nLEAVE")
                print("How do you wish to fight " + enemy.sName + "?\n")
                #fight_command = input("> ")
                #fight_command = normalise_input(fight_command)
                
                playerTurn = True
                
                while(playerTurn):
                    fight_command = input("> ")
                    fight_command = normalise_input(fight_command)
                    
                    if execute_fight_command(fight_command, enemy):
                        playerTurn = False
                        break
                    else: 
                        playerTurn = True
                    
                if player.bIsAWimp:
                    player.bIsAWimp = False
                    return
                else:
                    enemy_attack(enemy)
                if enemy.iHealth <= 0:
                    enemy.bAlive = False
                    enemy.die(player)
                
                player.checkDeath()
                print("\n=====================================\n\n")
                
    if(player.isAlive):
        print("Success! " + enemy.sName + " has been defeated.")
        print("\n=====================================\n\n")

def execute_attack(weapon, enemy):
    global hit_success
    hit_success = False
        
    if(weapon.upper() in "HANDS"):
        player.slapTheShitOutOf(enemy)
        hit_success = True
        return
        
    for item in player.inventory:
        #if getattritem:
        #    print("Can't attack with that item!")
        #    return
        
        try:
            if weapon.upper() in item.sName.upper():
                item.performAttack(player, enemy)
                hit_success = True
                if item.bFinite:
                    item.deplete(player)
                return
        except AttributeError:
            print("You can't attack with that item!")
            return

def execute_leave():
    if random.randrange(0, 100) > 50:
        player.bIsAWimp = True
        print("You escaped the fight successfully.")
    else:
        print("Escape failed!")
        print(player.name, " hurt themselves in confusion!")
        player.health -= 10
        player.checkDeath()
        
def enemy_attack(enemy):
        #total_dmg = (enemy["damage"] - random.randrange(0, player["resilience"]))
        #print(enemy["name"], "attacks the player for", total_dmg, "damage")
        #player["health"] -= total_dmg
        
        if hit_success:
            enemy.performAttack(player)
        
        # ask question
        # auto respond w/ answer
        # if wrong, take damage to hp and sanity
        # if right, take small damage to sanity (10%)
        
        #totalDmg = enemy.iAttackDamage
        #player.modSanity(DELTA)


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            print_inventory_items(player.inventory)

    elif command[0] == "use":
        if len(command) > 1:
            execute_useitem(command[1])
        else:
            print("Use what?")
            print_inventory_items(player.inventory)
    
    elif command[0] == "fight":
        count = 0
        for item in player.inventory:
            if item.sName == "Survey":
                count = item.iQuantity
                break 
        
        if len(command) > 1:
            if(command[1].upper() != Boss.sName or count >= 8):
                fight_loop(command[1])
            else:
                print("You require all 8 survey results to fight the Algorithm!")
        else:
            print("Fight who?")

    elif command[0] == "print":
        if len(command) > 1:
            buy_book(command[1])
        else:
            print("Print what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    
    global player
    player = Player()
    
    global winCond
    winCond = False
    
    print_room(player.current_room)
    
    # Main game loop
    while player.isAlive() and not winCond:
        #if current_room == rooms["Tutor"] and current_room["items"]==[item_pen]:
        print_inventory_items(player.inventory)

        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)

        # Execute the player's command
        execute_command(command)
        player.checkDeath()
        if player.current_room["name"] == "A Brightly Lit Room":
            player.health = 0
        
        print("\n=====================================\n\n")
        
        winCond = player.checkWin()
    
    if(winCond and player.isAlive()):
        print("""You wake up dazed and confused! And notice only a minute has passed since you’ve last looked at the clock. You remember the dream you’ve just had and sign in relief as you successfully completed your goal! But wait was that a dream, or did you really get the final surveys… 
To be continued""")


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
