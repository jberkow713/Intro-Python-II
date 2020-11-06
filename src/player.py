# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, level, lives,  magic_level,  room, item=[]):
        self.room = room 
        self.name = name
        self.item = item
        self.level = level
        
        self.magic_level = magic_level
        self.lives = lives
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    

   



