from itemsgame import *
from enemies import *
from itemsgame_OO import *
from enemies_OO import *

# TODO: Descriptions
room_1 = {"name":"Library",
          "description":
"""You enter a giant library. Books line the shelves for as far as you can see.\nThe library is eerily silent, you can't even hear your footsteps beneath you.\nA stale musk fills the air, like the air has not moved in centuries.\nYou make your way through the seemingly endless library,\nlooking for anything, something. Somebody is in the room with you...""",
          "exits":{"north":"Amazon Rainforest", "south":"Outside","east": "Reception", "west": "Cafe"},
          "items":[Printer()],
          "enemies": [Alex]
          }
room_2 = {"name": "Amazon Rainforest",
          "description": 
"""You have now entered your dream in a place that you don't recognise.\nYou can hear the sounds of birds, insects and the rustle of the trees that\nyou have just realised are surrounding you in every direction! To your amazement\nyou see an Amazon kingfisher, which means you must be in the Amazon Rainforest!\nWhy?! I don't know, it's your dream.""",
          "exits": { "south": "Library", "west": "The White House", "east": "A Brightly Lit Room"},
          "items": [],
          "enemies": []
          }
room_3 = {"name": "Reception",
          "description": "You find yourself in an office reception.\nThe desk is deserted, and nobody is in the room.\nYou try ringing the small metallic bell on the welcome desk, and wait.\nNobody appears.\nLooking around the room you spot a small TV in the corner,\nbut it is not tuned to anything,\nthe sound of white noise makes the room almost deafening.",
          "exits": { "west": "Library"},
          "items": [],
          "enemies": []
          }
room_4 = {"name": "Outside",
          "description": "You step outside. It is a brisk winter evening, and the cold seeps into your bones.\nYou catch your breath and consider the sky.\nIt's bleak and dark,\nwith a mountain of grey clouds rolling off towards the horizon.\nYou look around you and notice you are in a city centre.\nBut something is wrong, there is nobody here.\nThere is a silhouette leaning against one of the buildings...",
          "exits": {"north": "Library",  "east": "Corridor", "west": "Windows Lab"},
          "items": [],
          "enemies": [Bradley]
          }
room_5 = {"name": "Cafe",
          "description": "You step into a small, cosy café.\nThe bell above the door chimes sweetly as it closes behind you.\nYou instantly realise how pleasantly warm it is inside\nand you can feel your worries melt away.\nThe aroma of freshly ground coffee and baked pastries\nmakes its way into your nose,and you gratefully take it in.\nYou take a short break in one of the comfy seats, before continuing on your way.",
          "exits": {"east": "Library"},
          "items": [Coffee(5)],
          "enemies": [Neo]
          }
room_6 = {"name": "The White House",
          "description": "Yes seriously, you are in THE Whitehouse!\nThe oval office to be exact.\nLuckily there aren't any security guards as Trump doesn't seem to be home.\nYou can feel the tension of centuries of debates and arguments made in this room.\nAnd can't help wondering the enormous amount of secrets it could reveal.\nIsn't The Whitehouse known for secret passages? or is that somewhere else...",
          "exits": {"east": "Amazon Rainforest", "shortcut": "Bottom Of The Stairs"},
          "items": [Cigarette()],
          "enemies": [Alfie]
          }
room_7 = {"name": "Windows Lab",
          "description": "You are in Windows lab.\nThe faint glow of computer monitors illuminates the room.\nAfter surveying the room, you do not see anybody else here.\nYou peek at one of the monitors, but it just shows a log in screen.\nBeing in here brings back memories of staying up super late in labs\nlike these to ensure you finished your coursework on time,\nafter you had procrastinated it for two weeks.\nBut you shake it off and continue.",
          "exits": {"south": "Bottom Of The Stairs", "east": "Outside"},
          "items": [],
          "enemies": []
          }
room_8 = {"name": "Corridor",
          "description": "You find yourself in a long corridor.\nThe walls are dark,\nand they seem to get darker as you make your way down the corridor.\nThe soft carpet gives way beneath you,\nand it feels as if you are sinking deeper with each step that you take.\nYou try one of the many doors lining the corridor,\nbut the handle doesn't even seem to turn.\nYou spot someone standing in front of the door at the end of the corridor...",
          "exits": {"south": "Kirill's Office","west": "Outside"},
          "items": [],
          "enemies": [Josh]
          }
room_9 = {"name": "Bottom Of The Stairs",
          "description": "You are at the bottom of a staircase.\nYou peer up at the stairs, they seem to last an eternity and you feel dizzy just looking at it.\nThere are several exits surrounding you.\nYou feel trapped at the bottom of these stairs,\nso you start making your way towards one of the exits.\nBut you feel uneasy, as if somebody is watching you.\nOut of the corner of your eye, you realise someone is here with you...",
          "exits": {"north": "Windows Lab", "shortcut": "The White House","south": "Lecture Theatre", "east": "Kirill's Office"},
          "items": [],
          "enemies": [Matthew]
          }
room_10 = {"name": "Kirill's Office",
          "description": "You step into your office.\nYou instantly feel at ease being in familiar surroundings.\nYou switch your light on and look around the room.\nLooking at the bookshelf, you recognise all your books sitting there neatly,\nbut you cannot remember any of them.\nA stack of papers is sitting on your desk,\nbut you do not remember putting them there.\nAs you step closer, your desk chair spins around.\nSomebody was sitting in your chair...",
          "exits": {"north": "Corridor", "east": "Senghennydd Court", "west": "Bottom Of The Stairs"},
          "items": [Vape()],
           "enemies": [Morgan]
          }
room_11 = {"name": "Senghennydd Court",
          "description": "You are in Senghennydd Court.\nIt is a cold morning, with the sun scattering the sky a crimson red.\nPeople are walking around, and you try to get anyone's attention.\nNobody takes notice of you, as if you were invisible.\nYou sigh out in frustration, but you notice something.\nThere is someone in the crowd you has been looking directly at you...\nwithout taking notice of anybody else...",
          "exits": {"west": "Kirill's Office"},
          "items": [Coffee(2)],
          "enemies": [Tarek]
          }

room_12 = {"name": "The Lecture Theatre",
           "description": "You enter the lecture theatre; the large doors close abruptly behind you.\nYou didn't realise a place you have been in so many times previously,\ncould make you feel so nervous.\nYou take a deep breath, and you make your way down the steps.\nAfter all you've been through, you are ready to get this over with.\nYou cannot believe who you have to fight,\nbut you are prepared for the final fight...",
           "exits": {"north": "Bottom Of The Stairs"},
           "items": [],
           "enemies": [Boss]
           }

room_13 = {"name": "A Brightly Lit Room",
           "description": "You've moved into a completely different part of the dream,\na part that doesn't feel right.\nYou are surrounded by a blinding white light\nin the background you can hear faintly  the intro to Rupaul's drag race.\nThere is a tall bookcase standing right next to you and a large stage in front of you,\nwith what it looks like to be the famous Laganja Estranja.\nBefore you can express your amazement,\nshe performs a KILLER DEATH DROP!\nNo seriously it's KILLER, as it causes the bookcase to fall and crush you.",
           "exits": {"north": "Amazon Rainforest"},#none comes back from the dead
           "items": [],
           "enemies": []
           }


rooms = {
    "Library": room_1,
    "Amazon Rainforest": room_2,
    "Reception": room_3,
    "Outside": room_4,
    "Cafe": room_5,
    "The White House": room_6,
    "Windows Lab": room_7,
    "Corridor": room_8,
    "Bottom Of The Stairs": room_9,
    "Kirill's Office": room_10,
    "Senghennydd Court": room_11,
    "Lecture Theatre": room_12,
    "A Brightly Lit Room": room_13

}
