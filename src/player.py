# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, room):
        self.room = room 
        self.name = name

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)    




