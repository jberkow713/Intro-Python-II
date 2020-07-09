# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room 


class Player:
    def __init__(self, name, room, item=[]):
        self.room = room 
        self.name = name
        self.item = item
        

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    

    def add_item(self, item_choice):
          
        self.item.append(item_choice) 





