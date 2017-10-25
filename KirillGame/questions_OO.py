class Question():
    
    # Harder and more repetitive/annoying questions have a higher damage multiplier
    # The multiplier affects the damage by the enemy, which overall is resisted by the player's sanity
    fDamageMultiplier = 1.0
    fDifficulty = 0.5
    sQuestion = "NONE"
    
    # Potential answers
    sAnswers = [] 
    
    def __init__(self, diff, mult, qu, an):
        self.fDifficulty = diff
        self.fDamageMultiplier = mult
        self.sQuestion = qu
        self.sAnswers = an
        
        
# NOTE: Answers should ONLY be the correct/acceptable answers. Incorrect answers will be substituted with things like "I'm not sure" during combat. -Alex

# Difficulty, damage multiplier, question, answer
questionsList = [
    # Medium-difficulty question
    Question(0.5, 1.0, "How do I instance an object in Python?", ["You type the class name with parentheses, just like a method!", "Use the object name to initialise an instance!"]),
    
    # Hard, but may go by different terms for different people, so lower than full damage.
    Question(0.7, 0.8, "What's a C-Style comment?", ["Use a forward slashes with asterisks on the insides to comment a block of code", "Like this: /* todo */"]),
    
    # Opinionated question, slightly hard but lower-than-full damage.
    Question(0.5, 0.5, "Is C++ better than C?", ["It depends on the situation.", "C++ is better for software programming, but C is better for graphics programming."]),
    
    # Easy question, thusly a 30% damage increase if you get it wrong
    Question(0.25, 1.3, "Is Python a dynamically-typed language?", ["Yes.", "That is correct."]),
    
    Question(0.35, 1.2, "How strong is Python's typing?", ["Weak.", "Python is a weak-typed language."]),
    
    Question(0.15, 1.4, "What is Python?", ["A Scripting language that broke containment and is now loose in the streets of Manhattan, pretending to be a real language."]),
    
    # Maximum difficulty, so very small damage for getting it wrong.
    Question(1.0, 0.35, "How should I go about simulating a deformable bio-mechanical object in a realistic manner, in real-time?", ["By using a learnt statistical model to capture the idiosyncratic characteristics of the soft-body's dynamics and kinematics"]),
    
    Question(0.25, 1.2, "What was the first mechanical calculator?", ["The Pascaline, which was invented in 1642!", "The Pascaline, invented in 1642."]),

    Question(0.5, 1.0, "Does Moore's law still apply today?", ["Well, this is a debate as some people say that it is no longer economically viable to make transistors smaller"]),
    
    Question(0.20, 1.1, "How many buses are there in the system bus and what are their names?", ["There are three buses, the contol, the address and the data bus"]),
    
    Question(0.40, 0.9, "When was the first time that Cardiff University was attacked by a virus", ["It was in January of 1990 when the university used to be called Universtity College Cardiff", "In Winter of 1990, back when we were called University College Cardiff"]),
    
    
    Question(0.25, 1.2, "What are the effects of the Cascade virus?", ["All the characters fall to the bottom screen into a pile."]),
    
    Question(0.5, 0.9, "What is the 'code red' worm?", ["The Code Red worm is self-replicating malicious code that exploits a known vulnerability in Microsoft IIS servers"])
    ]

answerFailureStrings = [
    "I'm... not sure",
    "I don't know.",
    "You should know that!",
    "That's beyond me."
    ]