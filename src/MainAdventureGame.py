from room import Room
from player import Player 
# Declare all the rooms

room = {
'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Body Armor" ], ["There are no enemies here..."]),

'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["sword", "helmet"], ["Snakes...why did it have to be snakes?"]),

'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["key", "bomb"], ["Out of nowhere come three scary goblins"]),

'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["bow", "arrows"], ["A group of Mummies lumber towards you"]),

'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. """, ["diamond", "Arkenstone"], ["A giant Red Dragon approaches"]),

'Cave Exit': Room("Cave Exit", """You have free solod your way out of the treasure room to the opening above, 
the sun greets you as you claw your way through the rocks to a giant open field""", ["Spear"]),

'Enchanted Forest': Room("Enchanted Forest", """As you enter the woods you feel a bit funny...You turn around to 
retreat, only to find that you are completely lost""", ['Ocarina', 'Bag of marbles'], ['From the treetops, a giant spider \
descends upon you!']),

'Magical Entrance': Room("Magical Entrance", """The forest has captured you and brought you here...A world of wonder and magic
await you now! Beware the beasts that dwell within!""", ['Magic Cloak', 'Crystal Sword', 'Wand of Death']),

'Cauldron Room': Room("Cauldron Room", """In the center of the room lies a large cauldron...it is bubbling.""",
['Broomstick', 'Glowing Candle'], ['As you enter the room, a witch flies down from the ceiling to attack you!']),

'Wizard training room':Room("Wizard Training Room", """Wizards are battling it out in the corner...they spot you...""", 
['Enchanted Staff', 'Boomerang'], ['The head Wizard aims his wand at you'])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['Cave Exit']
room['Cave Exit'].s_to = room['treasure']
room['Cave Exit'].e_to = room['Enchanted Forest']
room['Enchanted Forest'].magic_to = room['Magical Entrance']
room['Magical Entrance'].n_to = room['Cauldron Room']
room['Cauldron Room'].s_to = room['Magical Entrance']
room['Magical Entrance'].e_to =room['Wizard training room']
room['Wizard training room'].w_to = room['Magical Entrance']






Link = Player(name='Link', level=1, magic_level=1, hitpoints=100, room=room["outside"], item=[] ) 
#print(Link)



# name = input("ENTER YOUR NAME!") 
# player = Player(name=name, room=room["outside"])
player = Link
print(f"Welcome {player.name}")

while True:

    print('----------------------------------------')
    users_choice = input("Please choose north, east, west, south, or magic: ")
    print('----------------------------------------')
        
    if users_choice == "q":
        print("Your journey has ended!")
        break
        
    if users_choice == "north":
        if player.room.n_to is not None:
            player.room = player.room.n_to
            print(player.room.description)
            print('----------------------------------------')
            if len(player.room.enemies) >=1:
                print(f" {player.room.enemies}")
                print('----------------------------------------')
            print(f"You find {player.room.item}")
            item_choice = input("Which item will you pickup?: \n")
            
            if item_choice in player.room.item and item_choice not in player.item:
            
                    if len(player.item) >= 5:
                        print("You currently have too many items in your bag")
                        print(f"You currently possess {player.item}")
                        swap_choice = input("Please choose an item to swap from your bag: ")
                        if swap_choice in player.item:
                            
                            player.item.remove(swap_choice)
                            player.item.append(item_choice)
                            
                            print(f"You currently possess {player.item}")
                        else:
                            print("You did not properly select an item to swap...better luck next time!")    
                    
                    elif len(player.item) <5:
                        print(f"You have added {item_choice}\n")
                        player.item.append(item_choice)
                        print(f"You currently possess {player.item}")
            elif item_choice in player.room.item and item_choice in player.item:
                print("You may only carry one of that item")
                continue
            else:
                print("You did not choose a proper item, better luck next time!")
                print(f"You currently possess {player.item}")
                continue   
            
            
            
            
        else:
            print('You can not go in that direction!')
            continue
   
    if users_choice == "south":
        if player.room.s_to is not None:
            player.room = player.room.s_to
            print(player.room.description)
            print('----------------------------------------')
            if len(player.room.enemies) >=1:
                print(f" {player.room.enemies}")
                print('----------------------------------------')
            print(f"You find {player.room.item}")
            item_choice = input("Which item will you pickup?: \n")
            
            if item_choice in player.room.item and item_choice not in player.item:
            
                    if len(player.item) >= 5:
                        print("You currently have too many items in your bag")
                        print(f"You currently possess {player.item}")
                        swap_choice = input("Please choose an item to swap from your bag: ")
                        if swap_choice in player.item:
                            player.item.remove(swap_choice)
                            player.item.append(item_choice)
                            
                            print(f"You currently possess {player.item}")
                        else:
                            print("You did not properly select an item to swap...better luck next time!")    
                    
                    elif len(player.item) <5:
                        print(f"You have added {item_choice}\n")
                        player.item.append(item_choice)
                        print(f"You currently possess {player.item}")
            
            elif item_choice in player.room.item and item_choice in player.item:
                print("You may only carry one of that item")
                continue
            
            else:
                print("You did not choose a proper item, better luck next time!")
                print(f"You currently possess {player.item}")
                continue   
            
                                    
            
        else:
            print('You can not go in that direction!')
            continue
          

             
    if users_choice == "west":
        if player.room.w_to is not None:
            player.room = player.room.w_to
            print(player.room.description)
            print('----------------------------------------')
            if len(player.room.enemies) >=1:
                print(f" {player.room.enemies}")
                print('----------------------------------------')
            print(f"You find {player.room.item}")
            item_choice = input("Which item will you pickup?: \n")
            
            if item_choice in player.room.item and item_choice not in player.item:
            
                    if len(player.item) >= 5:
                        print("You currently have too many items in your bag")
                        print(f"You currently possess {player.item}")
                        swap_choice = input("Please choose an item to swap from your bag: ")
                        if swap_choice in player.item:
                            player.item.remove(swap_choice)
                            player.item.append(item_choice)
                            
                            print(f"You currently possess {player.item}")
                        else:
                            print("You did not properly select an item to swap...better luck next time!")    
                    
                    elif len(player.item) <5:
                        print(f"You have added {item_choice}\n")
                        player.item.append(item_choice)
                        print(f"You currently possess {player.item}")
            elif item_choice in player.room.item and item_choice in player.item:
                print("You may only carry one of that item")
                continue
            else:
                print("You did not choose a proper item, better luck next time!")
                print(f"You currently possess {player.item}")
                continue   
        else:
            print('You can not go in that direction!')
            continue
             
    if users_choice == "east":
        if player.room.e_to is not  None:
            player.room = player.room.e_to
            print(player.room.description)
            print('----------------------------------------')
            if len(player.room.enemies) >=1:
                print(f" {player.room.enemies}")
                print('----------------------------------------')
            print(f"You find {player.room.item}")
            item_choice = input("Which item will you pickup?: \n")
            
            if item_choice in player.room.item and item_choice not in player.item:
            
                    if len(player.item) >= 5:
                        print("You currently have too many items in your bag")
                        print(f"You currently possess {player.item}")
                        swap_choice = input("Please choose an item to swap from your bag: ")
                        if swap_choice in player.item:
                            player.item.remove(swap_choice)
                            player.item.append(item_choice)
                            
                            print(f"You currently possess {player.item}")
                        else:
                            print("You did not properly select an item to swap...better luck next time!")    
                    
                    elif len(player.item) <5:
                        print(f"You have added {item_choice}\n")
                        player.item.append(item_choice)
                        print(f"You currently possess {player.item}")
            elif item_choice in player.room.item and item_choice in player.item:
                print("You may only carry one of that item")
                continue
            else:
                print("You did not choose a proper item, better luck next time!")
                print(f"You currently possess {player.item}")
                continue   
        else:
            print('You can not go in that direction!')
            continue
    
    if users_choice == "magic":
        if player.room.magic_to is not None:
            player.room = player.room.magic_to
            print(player.room.description)
            print('----------------------------------------')
            if len(player.room.enemies) >=1:
                print(f" {player.room.enemies}")
                print('----------------------------------------')
            print(f"You find {player.room.item}")
            item_choice = input("Which item will you pickup?: \n")
            
            if item_choice in player.room.item and item_choice not in player.item:
            
                    if len(player.item) >= 5:
                        print("You currently have too many items in your bag")
                        print(f"You currently possess {player.item}")
                        swap_choice = input("Please choose an item to swap from your bag: ")
                        if swap_choice in player.item:
                            player.item.remove(swap_choice)
                            player.item.append(item_choice)
                            
                            print(f"You currently possess {player.item}")
                        else:
                            print("You did not properly select an item to swap...better luck next time!")    
                    
                    elif len(player.item) <5:
                        print(f"You have added {item_choice}\n")
                        player.item.append(item_choice)
                        print(f"You currently possess {player.item}")
            elif item_choice in player.room.item and item_choice in player.item:
                print("You may only carry one of that item")
                continue
            else:
                print("You did not choose a proper item, better luck next time!")
                print(f"You currently possess {player.item}")
                continue   
                  
        else:
            print('You can not go in that direction!')
            continue    
                    
