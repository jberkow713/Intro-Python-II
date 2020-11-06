# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, level, attack, magic_attack, lives, fortune, defense, magic_level,  room, item=[]):
        self.room = room 
        self.name = name
        self.item = item
        self.level = level
        self.attack = attack
        self.magic_attack = magic_attack 
        self.magic_level = magic_level
        self.lives = lives
        self.defense = defense
        self.fortune = fortune
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    

   



