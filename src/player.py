# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, level, magic_level, hitpoints, room, item=[]):
        self.room = room 
        self.name = name
        self.item = item
        self.level = level
        self.hitpoints = hitpoints
        self.magic_level = magic_level
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    

   



