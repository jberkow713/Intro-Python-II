from room import Room
from player import Player 
# Declare all the rooms
import random

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
#World 1
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
#World 2
room['Magical Entrance'].n_to = room['Cauldron Room']
room['Cauldron Room'].s_to = room['Magical Entrance']
room['Magical Entrance'].e_to =room['Wizard training room']
room['Wizard training room'].w_to = room['Magical Entrance']






Link = Player(name='Link', level=1, attack = 1,  fortune=1, magic_attack = 1, defense=1,  magic_level=1, \
    room=room["outside"], item=[] ) 

player = Link
print(f"Welcome {player.name}")
difficulty_choice = input("Please choose easy, medium, hard, or expert: \n")
player.set_lives(difficulty_choice)

while True:

    #based on inventory, so they must reset to 1 before entering a new room in case inventory changes
    player.attack = 1
    player.magic_attack = 1
    player.defense = 1
    


    if "Body Armor" in player.item:
        player.lives = player.lives * 1.1
    if "sword" in player.item:
        player.attack = player.attack * 1.1
    if "helmet" in player.item:
        player.defense = player.defense * 1.1  
    if "bomb" in player.item:
        player.attack = player.attack * 1.15
    if "bow" and "arrows" in player.item:
        player.attack = player.attack * 1.3
    if "diamond" in player.item:
        player.fortune = player.fortune * 1.1
    if "Arkenstone" in player.item:
        player.magic_attack = player.magic_attack * 1.2
    if "Spear" in player.item:
        player.attack = player.attack * 1.2
    if "Ocarina" in player.item:
        player.magic_level = player.magic_level * 1.2
    if "Bag of marbles" in player.item:
        player.fortune = player.fortune * 1.1
    if "Magic Cloak" in player.item:
        player.magic_attack = player.magic_attack * 1.15
    if "Crystal Sword" in player.item:
        player.attack = player.attack * 1.3
    if "Wand of Death" in player.item:
        player.magic_attack = player.magic_attack * 1.3
    if "Broomstick" in player.item:
        player.canfly=True 
    if "Glowing Candle" in player.item:
        player.magic_level = player.magic_level * 1.1
    if "Enchanted Staff" in player.item:
        player.magic_attack = player.magic_attack * 1.25
    if "Boomerang" in player.item:
        player.attack = player.attack * 1.15            
                                
    #Continue here            








    #lives, level, and magic level are based on experience and defeating monsters, they can not reset
    # player.lives = round((player.lives * player.level * player.magic_level),1)
    print(f"Your current level is {round(player.level, 1)}, your current magic level is {round(player.magic_level,1)}")
    print(f"You currently have {player.lives} lives left.")
    print(f"Your current attack is {round(player.attack,1)}, your current magic attack is {round(player.magic_attack,1)}")
    print(f"Your current defense is {round(player.defense,1)}")

    print('----------------------------------------')
    users_choice = input("Please choose north, east, west, south, or magic: ")
    print('----------------------------------------')
    
    choices = ["north", "east", "west", "south", "magic"]
    directions = [player.room.n_to, player.room.e_to, player.room.w_to, player.room.s_to, player.room.magic_to]
    path_dict = dict(zip(choices, directions))


    if users_choice == "q":
        print("Your journey has ended!")
        break
    #consolidated all directions into one for loop!    
    for key, value in path_dict.items():
        if users_choice == key:
            if value is not None:
                player.room = value
     
                print(player.room.description)
                print('----------------------------------------')
                if len(player.room.enemies) >=1:
                    print(f" {player.room.enemies}")
                    print('----------------------------------------')
                    #check if enemy exists
                    #check which room in to adapt the battle
                    if player.room.name  == "Foyer":
                        while player.lives > 0:
                            print(f"You have {player.lives} lives, let the battle begin!")
                            #attack is improved based on your inventory which improves attributes
                            attack = (random.randint(0, 10)) * player.attack * player.magic_attack * player.defense
                            print(f"You prepare to battle the snakes, with {round(attack,1)} power!")
                            if attack >= 2:
                                player.lives +=1
                                player.level +=.02
                                print("You have defeated the Snakes, you may continue on!")
                                break
                            else:
                                player.lives -=1
                                print("The snakes have bitten you!")
                        
                        print(f"You have {player.lives} lives left!")
                        #check to see if player died during battle
                        if player.lives  <= 0:
                            print("You have died to a few wimpy snakes!")

                            break 

                    elif player.room.name == "Grand Overlook":
                        while player.lives >0:
                            print(f"You have {player.lives} lives, let the battle begin!")

                            attack = (random.randint(0, 20)) * player.attack * player.magic_attack * player.defense
                            print(f"You prepare to battle the Goblins, with {round(attack,1)} power!")
                            if attack > 7:
                                player.lives +=1
                                player.level +=.04
                                player.magic_level +=.02
                                print("You have defeated the Goblins")
                                break                                  
                            else:
                                player.lives -=1
                                print("The Goblins have injured you with their knives!")
                        
                        print(f"You have {player.lives} lives left!")        
                        
                        if player.lives  <= 0:
                            print("The Goblins have smashed you to pieces!")                       
                            break 


                    elif player.room.name == "Narrow Passage":
                        while player.lives > 0:
                            print(f"You have {player.lives} lives, let the battle begin!")
                            
                            attack = (random.randint(0, 25)) * player.attack * player.magic_attack * player.defense 
                            print(f"You prepare to battle the lurking mummies, with {round(attack,1)} power!")
                            if attack > 10:
                                player.lives +=1
                                player.level +=.06
                                print("You have defeated the Mummies!")
                                break
                            else:
                                player.lives -=1
                                print("The mummies have begun to mummify you!")
                        
                        print(f"You have {player.lives} lives left!")
                        
                        if player.lives  <= 0:
                            print("The mummies have entombed you for eternity!")
                                            
                            break 

                    elif player.room.name == "Treasure Chamber":
                        while player.lives >0:
                            print(f"You have {player.lives} lives, let the battle begin!")

                            attack = (random.randint(0, 50)) * player.attack * player.magic_attack * player.defense 
                            print(f"You prepare to battle the giant beast, with {round(attack,1)} power!")
                            if attack >= 35:
                                player.lives +=1
                                player.level +=.1
                                player.magic_level +=.08
                                print("You have defeated the Dragon!")
                                break 
                            else:
                                player.lives -=1
                                print("The monstrous claws of the red beast descend upon your head!")

                        print(f"You have {player.lives} lives left!")     
                        
                        if player.lives  <= 0:
                            print("Fire reigns down upon your head, you have been engulfed in flames!")
                                            
                            break    
                    elif player.room.name == "Enchanted Forest":
                        while player.lives >0:
                            
                            print(f"You have {player.lives} lives, let the battle begin!")
                            attack = (random.randint(0,100)) * player.attack * player.magic_attack * player.defense 
                            print(f"You prepare to battle the evil spider, with {round(attack,1)} power!")
                            if attack >= 80:
                                player.lives +=1
                                player.level +=.15
                                player.magic_level +=.15
                                print("You have defeated the wretched monstrosity!")
                                break 
                            else:
                                player.lives -=1
                                print("The spider has you trapped in her web!")

                        print(f"You have {player.lives} lives left!")     
                        
                        if player.lives  <= 0:
                            print("The spider feasts upon your flesh!")
                                            
                            break    




                print(f"You find {player.room.item}")
                item_choice = input("Which item will you pickup?: \n")
                #can not pick up duplicate items
                if item_choice in player.room.item and item_choice not in player.item:
                        #so far inventory cap is 5, may change it as game goes along and more rooms are added 
                        if len(player.item) >= 5:
                            print("You currently have too many items in your bag")
                            print(f"You currently possess {player.item}")
                            swap_choice = input("Please choose an item to swap from your bag: ")
                            if swap_choice in player.item:
                                #replaces 5th item with new chosen item
                                player.item.remove(swap_choice)
                                player.item.append(item_choice)
                                
                                print(f"You currently possess {player.item}")
                            else:
                                print("You did not properly select an item to swap...better luck next time!")    
                        #if less than 5 items are in inventory, adds item
                        elif len(player.item) <5:
                            print(f"You have added {item_choice}\n")
                            player.item.append(item_choice)
                            print(f"You currently possess {player.item}")
                elif item_choice in player.room.item and item_choice in player.item:
                    print("You may only carry one of that item")
                    continue
                #if improperly typed, no item is added, may tweak in future
                else:
                    print("You did not choose a proper item, better luck next time!")
                    print(f"You currently possess {player.item}")
                    continue   
                
                
                
                
            else:
                print('You can not go in that direction!')
                continue