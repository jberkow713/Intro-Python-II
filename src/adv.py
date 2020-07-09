from room import Room
from player import Player 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

current_room = []  
Room1 = 'Outside Cave Entrance'
Room2 = 'Foyer'
Room3 = 'Grand Overlook'
Room4 = 'A Narrow Passage'
Room5 = 'the Treasure Chamber'  

player = Player(room=room["outside"])


while True:
  


#    Room1 = 'Outside Cave Entrance'
#    Room2 = 'Foyer'
#    Room3 = 'Grand Overlook'
#    Room4 = 'A Narrow Passage'
#    Room5 = 'the Treasure Chamber'

    #users_choice = input("Choose north, south, east, or west: ")
    #print(f"User chooses: {users_choice}")
    
    

    users_choice = input("Please choose north, east, west, or south: ")
        
    if users_choice == "q":
            print("Your journey has ended!")
            break

        
    if users_choice == "north":
            
            player.room = player.room.n_to
            print(player.room.description)
                


    elif users_choice != "north":
        
            current_room = Room1 
            print("Please choose a new direction")
            

    while current_room == Room2:
        users_choice = input("Please choose north, east, west, or south: ")
                                        
        if users_choice == "north":
            current_room = Room3
            print(f"You are in the {Room3}")
            print("A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
                    

        elif users_choice == "east":
            current_room = Room4
            print(f"You are in the {Room4}")
            print("The narrow passage bends here from west to north. The smell of gold permeates the air.")
                    

        elif users_choice == "south":
            print(f"You are in the {Room1}")
            print("North of you, the cave mount beckons")
            current_room = Room1

        elif users_choice == "west":
            current_room = Room2
            users_choice = input("Please choose a new direction: ") 
                    
        elif users_choice == "q":
            print("Your journey has ended!")
            break    
        
    while current_room == Room3:
        
        users_choice = input("Please choose north, east, west, or south: ") 
            
        if users_choice == "south":
            current_room = Room2 
            print(f"You are in the {Room2}")
            print("Dim light filters in from the south. Dusty passages run north and east.")
                    

        elif users_choice == "east":
            current_room = Room3
            
                    

        elif users_choice == "west":
            current_room = Room3 
            
                    

        elif users_choice == "north":
            current_room = Room3
             
                    

        elif users_choice == "q":
            print("Your journey has ended!")
            break   

    while current_room == Room4:
        users_choice = input("Please choose north, east, west, or south: ") 

        if users_choice == "west":
            current_room = Room2    
            print(f"You are in the {Room2}")
            print("Dim light filters in from the south. Dusty passages run north and east.")
                    
                    

        elif users_choice == "north":
            current_room = Room5
            print(f"You are in the {Room5}")
            print("You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")
                    
                    
                
        elif users_choice == "south":
            current_room = Room4
            users_choice = input("Please choose a new direction: ") 
                    

        elif users_choice == "east":
            current_room = Room4
            users_choice = input("Please choose a new direction: ") 
                    

        elif users_choice == "q":
            print("Your journey has ended!")
            break 

    while current_room == Room5:
        users_choice = input("Please choose north, east, west, or south: ")    

        if users_choice == "south":
            current_room = Room4
            print(f"You are in the {Room4}")
            print("The narrow passage bends here from west to north. The smell of gold permeates the air.")
                    

        elif users_choice != "south":
            current_room = Room5
            users_choice = input("Please choose a new direction: ") 
                    

        elif users_choice == "q":
            print("Your journey has ended!")
            break      

            













        #users_choice = input("Please choose north, east, west, or south: ")






           




        





    

        

        



    


        

        









    

    
        
        #player starts in outside room, can only move north to the Foyer
    
    # from the Foyer player can move north to overlook, east to narrow, 
    # south to outside
    
    #if moves to outside, can only move back north to Foyer

    #if moves to overlook, can only move back south to Foyer

    #if moves to narrow, can go west to Foyer, north to treasure room

    #if moves to treasure room, can go south to narrow








#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
