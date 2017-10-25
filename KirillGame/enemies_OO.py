#from game import printDebug
#from random import randint
#from numpy.random import choice
#from itemsgame_OO import *
#from questions_OO import *
#from math import ceil
#import random

from itemsgame_OO import *
from random import randint
from questions_OO import *
from math import ceil, pow
import random

class NPC:
    bAlive = True
    iHealth = 100
    iMaxHealth = iHealth
    inventory = []
    iAttackDamage = 25
    sName = "NO_NAME"
    sDesc = "NO_DESC"
    
    # Object type. Describes vulnerabilities, if any, to certain items    
    objVulnerability = None
    
    # The bonus damage taken when hit with an attack that they're vulnerable to
    # Defaults to 30%
    fVulnerabilityMult = 1.3
    
    def __init__(self, hp, inv, dmg, nm, dc, vuln):
        self.iHealth = hp
        self.iMaxHealth = hp
        self.inventory = inv
        self.iAttackDamage = dmg
        self.sName = nm
        self.sDesc = dc
        self.objVulnerability = vuln
        
    def performAttack(self, p):
        # A list of the questions sorted by difficulty
        sortedList = sorted(questionsList, key=lambda x: x.fDifficulty, reverse=False)
        i = randint(0, len(sortedList) - 1)       
        ceil((self.iAttackDamage / 40) * i)
        
        question = sortedList[i]
        #question = choice(sortedList, 1, p=(self.iAttackDamage / 40)
        
        print("##################################")
        print(self.sName + " asks a question!")
        print("> " + self.sName + ": " + question.sQuestion)

        probability = pow(-question.fDifficulty + 1, 1 - (p.intelligence / 100))
        
        success = random.random() < probability
        
        #print("PROBABILITY: " + str(probability))
        
        if success:
            print("> " + p.name + ": " + question.sAnswers[randint(0, len(question.sAnswers) - 1)])
            print("You evade the question successfully.")
            print("##################################")
        else:
            print("> " + p.name + ": " + answerFailureStrings[randint(0, len(answerFailureStrings) - 1)])
            # Damaged based on remaining sanity * attack damage * question damage multiplier
            p.damage(self.iAttackDamage * question.fDamageMultiplier * (1/ (p.sanity / 100)))
            
            # Sanity reduced based on inverse of question difficulty (question easiness) * attack damage
            p.modSanity(-ceil((1 / question.fDifficulty) * (self.iAttackDamage / 8)))
            print("##################################")
            print(p.name + " now has " + str(p.health) + " health, and " + str(p.sanity) + " sanity.")
            p.checkDeath()
        
    def die(self, player):
        # Iteratively add the stack of items to the world
        for item in self.inventory:
            for i in  range (0, item.iQuantity):
                player.current_room["items"].append(item)

# Health, inventory, damage, name, description, item vulnerability as a type (if any)
        
Alex = NPC(150, 
           [Survey(), Coffee(2), Textbook(), Printcred(2)], 
           15, 
           "Alex", 
           "A Computer science student with hard-hitting questions about your research! Vulnerable to being hit with a thesis.",
           Thesis
           ) 

Alfie = NPC(100, 
           [Survey(), Textbook(2), Printcred(2), Vape()], 
           35, 
           "Alfie", 
           "A Computer science student with a passion for performance arts! Vulnerable to unarmed slap attacks.",
           "TheseHands"
           )
Bradley = NPC(105, 
           [Survey(), Textbook(), Printcred(2), Cigarette()], 
           25, 
           "Bradley", 
           "A Computer science student, passionate about writing code in Python. Vulnerable to the handbook.",
           Handbook
           )

Josh = NPC(90, 
           [Survey(), Textbook(), Printcred(2), Coffee()], 
           30, 
           "Josh", 
           "A Computer science student who has lots of queries about how you analysed the survey results. Vulnerable to being hit with a thesis.",
           Thesis
           )

Matthew = NPC(140, 
           [Survey(), Textbook(), Printcred(), Vape()], 
           25, 
           "Matthew", 
           "A Computer science student ready to ask some tough questions.",
           None
           )

Morgan = NPC(120, 
           [Survey(), Textbook(2), Printcred(), Coffee()], 
           30, 
           "Morgan", 
           "A Computer science student that can make your life difficult if he starts complaining about the assessments. Vulnerable to textbooks.",
           Textbook
           )

Tarek = NPC(80, 
           [Survey(), Textbook(), Printcred(3), Cigarette(2)], 
           40, 
           "Tarek", 
           "A Computer science student who knows how to fight.",
           None
           )

Neo = NPC(125, 
           [Survey(), Textbook(), Printcred(2), Vape()], 
           25, 
           "Neo", 
           "A Computer science student with lots of silly questions to irritate you with.",
           None
           )

Boss = NPC(200,
           [Cigarette()],
           45,
           "Algorithm",
           "A 32-Dimensional questionnaire evaluating method. Grand in appearance. Intimidating in volume. Genius in design. No vulnerabilities.",
           None
           )
