item_handbook = {
    "id": "handbook",
    
    
    "name": """
    Handbook""",

    
    "description": """

Objective: Your aim is to collect about 10 surveys from students, so that you can complete your graphs. To get the surveys, you must answer a series of questions from each student.

Commands:

Type “go <direction>” in order to move your character to that area.
Type “use <item>” to use one of your items from your inventory.
Type “drop <item>” to drop an item from your inventory, into the room.
Type “fight <student name>” to start the battle with student. (where there is a student in the room)
Type “print <book/thesis>” to print a book or thesis. (only available in the library)
In combat:
Type “attack with <item>” to attack with that item.
Type “use <item>” to use that item.
Type “leave” to flee from the fight.


Items:

Handbook: Your main weapon for fighting.
Cigarette: Replenishes sanity, but reduces health. (only usable outdoors)
Vape: Replenishes sanity, no effect to health. (only usable outdoors)
Book: Stronger weapon for fighting.
Thesis: Strongest weapon for fighting.
Survey: Your reward for defeating the students, needed to win the game.
Print credits: Currency used to print books/thesis. (only usable in the library)
Coffee: Replenishes health.""",
    
    
    "mass": 0,
    "damage": 30,
    "bIsFinite":False
}


item_cig = {
    "id": "cigarette",

    "name": "Cigarette",

    "description": "Replenishes your sanity, reduces health. No smoking indoors.",
    "mass": 50,
    "damage": 0,
    "iSelfdamage":1,
    "iSanityRestore":2,
    "bIsFinite":True
}

item_vape = {
    "id": "vape",

    "name": "E-Cigarette",

    "description": "Replenishes your sanity less than a cigarette, but without damaging health. No smoking indoors.",
    "mass": 80,
    "damage": 0,
    "iSanityRestore":1,
    "bIsFinite":False
}


item_book = {
    "id": "book",

    "name": "Book",

    "description": "Single-use. Can be used to attack an enemy, or can be read to increase intelligence.",
    
    "mass": 400,
    "damage": 25,
    "iIntelligence":1,
    "bIsFinite":True
}


item_printcred = {
    "id": "print credits",

    "name": "Print Credits",

    "description": "With this you can print books or theses.",
    
    "mass": 0,
    "damage": 0,
    "bIsFinite":True
}


item_coffee = {
    "id": "coffee",

    "name": "Cup of coffee",

    "description": "Refreshing, restores health.",
    
    "mass": 100,
    "damage": 0,
    "iHealthRestore": 3,
    "bIsFinite":True
}



item_survey = {
    "id": "survey",
    
    "name": "Completed background survey",

    "description": "The elusive answers to the background survey.",
    "mass": 50,
    "damage": 1,
    "bIsFinite":False
}

item_thesis = {
    "id": "Thesis",
    
    "name": "Learnt Real-time Meshless Simulation",

    "description": "The paper's abstract explains a novel approach to simulating realistic soft-bodies in Computer Graphics.",
    "mass": 150,
    "damage": 99,
    "iIntelligence": 5,
    "bIsFinite":True
}

# Abstract - not an item, but a device usable by the player.
# This really shouldn't be an item.
item_shop = {
    "id": "Printer",
    "name": "Printer for printing publications",
    "Description": "Printed books can be read or used to attack.",
    # Note: This is not a quantity of how many the shop has, but instead the cost (in print credits)
    "inventory": (item_book, item_thesis),
    "costs": (1, 5)
}






