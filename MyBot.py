#!/usr/bin/env python
from ants import *

# define a class with a do_turn method
# the Ants.run method will parse and update bot input
# it will also run the do_turn method for us
class MyBot:
    def __init__(self):
        pass
        
    def do_setup(self, ants):
        self.my_ants = []
        self.destinations = []
        for position in ants.my_ants():
            self.my_ants.append(Ant(ants, position, self))



    def do_turn(self, ants):
        #update my_ants
        for position in ants.my_ants():
            ants_i_already_have = set([ant.position for ant in self.my_ants])
            if not position in ants_i_already_have:
                self.my_ants.append(Ant(ants, position, self))
            

        for ant in self.my_ants:
            ant.update()
            
class Ant:
    def __init__(self, ants, pos, bot):
        self.bot = bot
        self.position = pos
        self.ants = ants
        self.new_position = None
        self.order = None
        self.destination = None
        self.distance_to_destination = None

    def update(self):
        with open("log.txt", "a") as f:
            f.write(str(self.destination)+"==")
            f.write(str(self.position))
            f.write("\n")
        if self.destination == self.position:
            self.destination = None
            with open("log.txt", "a") as f:
                f.write("\tTrue")
                f.write("\n")

            
        if not self.destination:
            self.distance_to_destination, x, self.destination = self.search_for_food()
        

        self.move()
    

    def move(self):
        direction_to_move = None
        
        for direction in self.ants.direction(self.position, self.destination):
            self.new_position = self.ants.destination(self.position, direction)
                        
            if self.ants.unoccupied(self.new_position):
                self.ants.issue_order((self.position, direction))
                self.position = self.new_position
    
    def search_for_food(self):
        food_list = []
        
        for food_position in self.ants.food():
            dist = self.ants.distance(self.position, food_position)
            food_list.append((dist, self.position, food_position))
        food_list.sort()

        return food_list.pop()
                
    

    def execute(self):
        if self.order == "move": self.move()
        

    def explore(self):
        pass
    

    def calculate_path_to_position(self, target, force=False):
        pass

class Map:
    def __init(self, ants):
        pass
    
    
        
if __name__ == '__main__':
    # psyco will speed up python a little, but is not needed
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    try:
        # if run is passed a class with a do_turn method, it will do the work
        # this is not needed, in which case you will need to write your own
        # parsing function and your own game state class
        Ants.run(MyBot())
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')
