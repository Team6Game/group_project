from playergame import *

class GenericItem:
    # Can the item be used? 
    bUsable = True
    
    bFinite = True
    
    # Can the item be in the player's inventory?
    bPlayerInventoryAllowed = True
    
    # Can the item be used when attacking?
    bIsWeapon = False
    
    # Mass in grams
    fMass = 0
    
    iQuantity = 1
    
    #self.sID = "NO_ID"
    sName = ""
    sDesc = ""
    
    def __init__(self, usable = True, invAllow = True, wep = False, mass = 0, quantity = 1, nm = "NO_NAME",  desc = "NO_DESC"):
        self.bUsable = usable
        self.bPlayerInventoryAllowed = invAllow
        self.bIsWeapon = wep
        self.fMass = mass
        self.iQuantity = quantity
        self.sName = nm
        self.sDesc = desc
        
    # To be overridden in subclasses
    # Takes only a player as an argument
    def useItem(self, p):
        pass
    
    def deplete(self, p):
        print("You discard the used item.")
        self.iQuantity -= 1
        if self.iQuantity <= 0:
            print("You have used all of this item!")
            p.inventory.remove(self)
            
    def add(self):
        print("You add the item to your inventory.")
        self.iQuantity += 1
        p.inventory.append(self)

    # These two functions are required by Python in order to use GenericItem as a key in the player's inventory
    # Keys must be unique, and so I must provide functions to hash the object, and to equate it.
    def __hash__(self):
        # Name and description ought to be unique on each item, so this will do.
        # If not, we can add more of its attributes to the hash.
        return hash((self.sName, self.sDesc))

    def __eq__(self, other):
        # Equality check
        return (self.sName, self.sDesc) == (other.sName, other.sDesc)

class Weapon(GenericItem):
    
    # Int damage to decide health loss on hit
    fDamage = 1
    
    def __init__(self, name, desc, damage, m):
        # Explicitly true, if only Python has constants or read-onlys... or pointers, or real blocks, or anything.
        super().__init__(wep = True, invAllow = True, nm=name, desc=desc, mass=m)
        self.fDamage = damage
        
    # To be overridden in subclasses to allow generic calling of an attack function
    def performAttack(self, p, e):
        pass

class Consumable(GenericItem):
    fSanityRestored = 0
    fHealthRestored = 0
    
    def __init__(self, n, d, m, q=1):
        super().__init__(True, True, True, m, q, n, d)
        bFinite = True
        
    def useItem(self, p):
        p.heal(self.fHealthRestored)
        p.modSanity(self.fSanityRestored)
        p.checkDeath()
        print(p.name + " now has " + str(p.health) + " health, and " + str(p.sanity) + " sanity.")
    
class Coffee(Consumable):
    def __init__(self, q=1):
        super().__init__("Coffee", "A flask of coffee from Starbucks. The scrawled name on the side reads 'Kerry Ill'.", 500)
        self.fHealthRestored = 50
        self.fSanityRestored = 0
        self.iQuantity = q
    
    def useItem(self, p):
        super().useItem(p)
        print("After enjoying a nice cup of coffee you feel revitalised and awake. \nYour health has been restored")
        
class Cigarette(Consumable):
    def __init__(self, q=1):
        super().__init__(n='Cigarette', d='A single cigarette, self rolled.', m=50)
        self.fHealthRestored = -10
        self.fSanityRestored = 25
        self.iQuantity = q
    
    def useItem(self, p):
        from mapgame import rooms
        if p.current_room == rooms["Outside"]:
            super().useItem(p)
            print("You feel calmer now. \nYour sanity has been restored")
            print("But, your health has been drained.")
        else: 
            print ("You're not allowed to smoke indoors so your cigarette is taken away!")

class Vape(Consumable):
    def __init__(self, q=1):
        super().__init__(n='Vape', d='A charged vape pen.', m=150, q=1)
        self.fHealthRestored = 0
        self.fSanityRestored = 15
        self.iQuantity = q
        
    def useItem(self, p):
        from mapgame import rooms
        if p.current_room == rooms["Outside"]:
            super().useItem(p)
            print("You feel calmer now. \nYour sanity has been restored")
        else: 
            print ("You're not allowed to smoke indoors!")

        
class Book(Weapon):
    iIntelligenceBuff = 0
    iCost = 0
    
    def __init__(self, name, desc, damage, intelligence, cost, mass, q=1):
        super().__init__(name, desc, damage, mass)
        self.iIntelligenceBuff = intelligence
        self.iQuantity = q
        self.iCost = cost
        
    def useItem(self, p):
        p.intelligence += self.iIntelligenceBuff
        print("You read one of your printed books, bolstering your knowledge!")
        print("Intelligence increased to " + str(p.intelligence) + ".")
        
    def performAttack(self, p, e):
        # Subtracts from the enemy health the amount of damage we deal,
        # Multiplied by the vulnerability multiplier IF the enemy is 
        # vulnerable to our weapon
        e.iHealth -= self.fDamage * (e.fVulnerabilityMult if (e.objVulnerability == type(self)) else 1)
        print("You bludgeon " + e.sName + " with the publication, dealing " + str(self.fDamage * (e.fVulnerabilityMult if (e.objVulnerability == type(self)) else 1)) + " damage! ")
        print("It's super effective!" if e.objVulnerability == type(self) else "")


class Handbook(Weapon):
    def __init__(self, q=1):
        super().__init__("Handbook", "Handbook\n\nObjective: Your aim is to collect 8 surveys from students, so that you can complete your graphs and group allocations. To get the surveys, you must answer a series of questions from each student.\n\nCommands:\n\nType 'go <direction>' in order to move your character to that area.\nType 'use <item>' to use one of your items from your inventory.\nType 'drop <item>' to drop an item from your inventory, into the room.\nType 'fight <student name>' to start the battle with student. (where there is a student in the room)\nType 'print <book/thesis>' to print a book or thesis. (only available in the library)\nIn combat:\nType 'attack with <item>' to attack with that item.\nType 'use <item>' to use that item.\nType 'leave' to flee from the fight.\n\n\nItems:\n\nHandbook: Your guide, and a weapon for fighting.\nCigarette: Replenishes sanity, but reduces health. (only usable outdoors)\nVape: Replenishes sanity, no effect to health. (only usable outdoors)\nBook: Stronger weapon for fighting. Provides some intelligene when read.\nThesis: Strongest weapon for fighting, provides the most intelligence when read.\nSurvey: Your reward for defeating the students, needed to win the game.\nPrint credits: Currency used to print books/thesis. (only usable in the library)\nCoffee: Replenishes health.\n",
                         15,
                         400)
        self.iQuantity = q
        self.bFinite = False

    def useItem(self, p):
        print(self.sDesc)
    
    def performAttack(self, p, e):
        # Subtracts from the enemy health the amount of damage we deal,
        # Multiplied by the vulnerability multiplier IF the enemy is 
        # vulnerable to our weapon
        e.iHealth -= self.fDamage * (e.fVulnerabilityMult if (e.objVulnerability == type(self)) else 1)
        print("You bludgeon " + e.sName + " with the handbook, dealing " + str(self.fDamage * (e.fVulnerabilityMult if (e.objVulnerability == type(self)) else 1)) + " damage! ")
        print("It's super effective!" if e.objVulnerability == type(self) else "") 
        
class Thesis(Book):
    def __init__(self, q=1):
        super().__init__("Thesis", "'Learnt Real-time Meshless Simulation'. The paper's abstract explains a novel approach to simulating realistic soft-bodies in Computer Graphics. Can be used to attack, or can be read for bonus intelligence.", 75, 25, 5, mass = 400)
        self.iQuantity = q
        self.iCost = 5
        
    def useItem(self, p):
        p.intelligence += self.iIntelligenceBuff
        print("You re-read your thesis, vastly increasing your understanding of Computer Graphics and facial kinematics.")


class Textbook(Book):
    def __init__(self, quantity=1):
        super().__init__("Book", "'Introduction to Python' Textbook. Can be used to attack, or can be read for a small intelligence bonus", 30, 10, 1, mass = 250)
        self.iQuantity = quantity

class Printcred(GenericItem):
    def __init__(self, quantity=1):
        super().__init__(False, True, False, 5, 1, "Credit", "Can be used to print books in the library.")
        self.iQuantity = quantity
class Survey(GenericItem):
    def __init__(self, quantity=1):
        super().__init__(False, True, False, 0, quantity, "Survey", "The elusive results to the student background survey.")
        self.iQuantity = quantity
        
class Printer(GenericItem):
    def __init__(self):
        super().__init__(False, False, False, 0, 1, "Printer", "Can be use to print books and publications with print credits.")
        
