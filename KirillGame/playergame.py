from itemsgame import * 
from mapgame import rooms
import math
from random import randint
from itemsgame_OO import *
#from game import printDebug

# multiple items in inventory need to be fixed 
#inventory = [item_handbook, item_cig, item_cig]
#inventory = {item_handbook:1, item_cig:2, item_coffee:1}

#player = {}
#player["name"]= "Kirill"
#player["health"]= 900
#player["sanity"]= 50
#player["intelligence"]= 45
#player["alive"] = True


#total_mass = 1500

# Start game at the reception
#current_room = rooms["Amazon Rainforest"]




class Actor:
    name = ""
    health = 100
    sanity = 100
    intelligence = 15
    alive = True
    current_room = None
    # Item : Quantity
    inventory = {}
    
    def __init__(self, nameIn, healthIn, sanityIn, intelligenceIn):
        self.name = nameIn
        self.health = healthIn
        self.sanity = sanityIn
        self.intelligence = intelligenceIn
        pass
        
    def damage(self, dmg):
        self.health -= int(math.ceil(dmg * (self.sanity / 100)))
        self.checkDeath()
    
    def heal(self, dmg):
        self.damage(-dmg)
    
    def modSanity(self, delta):
        self.sanity += delta
    
    def addToInventory(self, item, count = 1):
        if item in inventory:
            self.inventory["item"] += count
        else:
            self.inventory["item"] = count
        
    def checkDeath(self):
        if(self.health <= 0 or self.sanity <= 0):
            self.alive = False
            # Death code here
            self.die()
            print(name + " has died.")
        else:
            self.alive = True
            
    def die(self):
        # Iteratively add the stack of items to the world
        for item, quantity in inventory.items():
            for i in  range (0, quantity):
                self.current_room["items"].append(item)

    def isAlive(self):
        self.checkDeath()
        return self.alive
        
    def performAnimation(self, loop = False):
        pass
    
class Player(Actor):
    
    # Enemy questions are answered based on player intelligence and question difficulty
    # Failing to answer a question lowers sanity and allows the enemy to hit you with an attack, with damage multiplied by the question's damage multiplier 
    # Answering a question successfully skips the enemy turn and allows you to make a move 
    # You can choose to attack or use an item on your turn
    # You can use items outside of combat, e.g. read a book, but it may not be strategically sound to do so (You don't know if you'll need the book to attack later, or whether you should read it for intelligence)
    
    slapDamage = 25
    
    mass = 0
    maxMass = 4000
    current_room = rooms["Amazon Rainforest"]
    
    # Josh's flag for leaving a fight
    bIsAWimp = False
    
    def __init__(self):
        Actor.__init__(self, "Kirill", 100, 50, 25)
        self.inventory = [Handbook(), Coffee(1), Cigarette(3), Printcred(1)]
        
    def checkDeath(self):
        if(self.health <= 0 or self.sanity <= 0):
            self.alive = False
            print("############################################")
            print("############## You have died. ##############")
            print("############################################")
            exit()
            
    def checkWin(self):
        for item in self.inventory:
            if(type(item) == Survey and item.iQuantity >= 8 and self.current_room == rooms["The Lecture Theatre"]):
                if(not current_room["enemies"][0].bAlive):
                    return True
                    
        return False
        
    def updateMass(self):
        tempmass = 0
        for item in self.inventory:
            tempmass += (item.fMass * item.iQuantity)
        #print("Player mass: " + str(tempmass))
        self.mass = tempmass
        return self.mass
    
    def checkOverEncumbered(self):
        #return self.updateMass() > self.maxMass
        return False # Screw carry-weights. We're not Bethesda.

    # Damages an enemy using bare hands
    def slap(self, enemy):
        enemy.iHealth -= self.slapDamage * (enemy.fVulnerabilityMult if (enemy.objVulnerability == type("These Hands")) else 1)
      
class Enemy(Actor):
    
    # 20 HP of damage each hit, adjusted for in the damage function with sanity
    attackStrength = 20
    
    def __init__(self, nameIn, healthIn, sanityIn, intelligenceIn):
        super().__init__(self, nameIn, healthIn, sanityIn, intelligenceIn)
        # Each enemy will carry between 0 and 3 print credits
        self.inventory[item_printcred] = randint(0, 3)
    
