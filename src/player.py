# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, level, attack, magic_attack, fortune, defense, magic_level,  room, item=[]):
        self.room = room 
        self.name = name
        self.item = item
        self.level = level
        self.attack = attack
        self.magic_attack = magic_attack 
        self.magic_level = magic_level
        # self.lives = 0
        self.defense = defense
        self.fortune = fortune
        self.canfly = False 
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    def set_lives(self, difficulty_choice):
        
        difficulty_levels = ["easy", "medium", "hard", "expert"]
        lives_choices = [15, 10, 6, 3]
        difficulty_dict = dict(zip(difficulty_levels, lives_choices))
        for key, value in difficulty_dict.items():
            if difficulty_choice == key:
                Player.lives = value  


    

   



