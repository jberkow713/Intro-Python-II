from room import Room
from player import Player 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["sword", "helmet"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["key", "bomb"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["bow", "arrows"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["diamond", "Arkenstone"]),
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




#
# Main
#
#Link = Player('outside', 'knight', 100)
#print(Link)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:


 # want to print current room and current description based on where the player is
 # so everytime player moves into new room, prints room player is in, and description of room

#current_room = []  
#Room1 = 'Outside Cave Entrance'
#Room2 = 'Foyer'
#Room3 = 'Grand Overlook'
#Room4 = 'A Narrow Passage'
#Room5 = 'the Treasure Chamber'  

name = input("ENTER YOUR NAME!")
player = Player(name, room['outside'], ) 
print(f"Welcome {player.name}")


print("Find treasure, and bring it out of the cave! Become rich beyond your wildest dreams!")
print("But Beward! Once you exit the cave, all of your riches will disappear!")
print("Choose your path Adventurer!")
print(player.room.description)



# add get item and drop item commands






while True:

  


#    Room1 = 'Outside Cave Entrance'
#    Room2 = 'Foyer'
#    Room3 = 'Grand Overlook'
#    Room4 = 'A Narrow Passage'
#    Room5 = 'the Treasure Chamber'

    #users_choice = input("Choose north, south, east, or west: ")
    #print(f"User chooses: {users_choice}")
    
    
    
    
    
    #item_choice = input("Which items will you pickup?: \n")
    #print(f"You have added {player.add_item}")
    #print(f"You now have {player.item}")
    users_choice = input("Please choose north, east, west, or south:")
    
    
    
    
    

     
    if users_choice == "q":
        print("Your journey has ended!")
        break

    if player.room == room['outside']:
        print(player.room.description)
        
        items = []
        
        if users_choice == "north":
            player.room = player.room.n_to
            print(player.room.description)
            print(f"You find {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
            
            
            print(f"You now have {items}")
            
            
            
    
        if users_choice == "south":
            print("Choose a new path")
        elif users_choice == "east":
            print("Choose a new path")  
        elif users_choice == "west":
            print("Choose a new path")      
        else:
            print("Choose a new path")


    elif player.room ==room['foyer']:


        if users_choice == "north":
            player.room = player.room.n_to
            print(player.room.description)
            print(f"You find  {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
                        
            print(f"You now have {items}")
            
        elif users_choice == "south":
            
            player.room = player.room.s_to
            print(player.room.description)
            print(f"You find  {player.room.item}")
            #item_choice = input("Which items will you pickup?: \n")
            #print(f"You have added {item_choice}\n")
            #items.append(item_choice)
            print(f"Your items disappear, thus is life, you should have stayed in the cave")
            
        elif users_choice == "east":
            player.room = player.room.e_to
            print(player.room.description)
            print(f"You find  {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
            print(f"You now have {items}")
            
        elif users_choice == "west":
            print("Choose a new path!")
        else:
            print("Choose a new path!")    

    elif player.room ==room['overlook']:

        if users_choice == "south":
           player.room = player.room.s_to
           print(player.room.description)
           print(f"You find  {player.room.item}")
           item_choice = input("Which items will you pickup?: \n")
           print(f"You have added {item_choice}\n")
           items.append(item_choice)
           print(f"You now have {items}")
           
        elif users_choice == "north":
            print("Choose a new path!")
        elif users_choice == "west":
            print("Choose a new path!")
        elif users_choice == "east":
            print("Choose a new path!")
        else:
            print("Choose a new path!")  

    elif player.room ==room['narrow']:

        if users_choice == "north":
            player.room = player.room.n_to
            print(player.room.description)
            print(f"You find  {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
            print(f"You now have {items}")
            
        elif users_choice == "west":
            player.room = player.room.w_to
            print(player.room.description)
            print(f"You find {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
            print(f"You now have {items}")
            
        elif users_choice == "east":
            print("Choose a new path!")
        elif users_choice == "south":
            print("Choose a new path!")  
        else:
            print("Choose a new path!")

    elif player.room ==room['treasure']:
        if users_choice == "south":
            player.room = player.room.s_to
            print(player.room.description)
            print(f"You find {player.room.item}")
            item_choice = input("Which items will you pickup?: \n")
            print(f"You have added {item_choice}\n")
            items.append(item_choice)
            print(f"You now have {items}")
            

        elif users_choice == "north":
            print("Choose a new path!")

        elif users_choice == "west":
            print("Choose a new path!")

        elif users_choice == "east":
            print("Choose a new path!") 
        else:
            print("Choose a new path!")                                


            
                          

             
                   
        

        

        


    
        #if users_choice == "east":

         #   player.room = player.room.e_to
          #  print(player.room.description)

    
        





