#!/usr/bin/env python
from ants import *
import random
# define a class with a do_turn method
# the Ants.run method will parse and update bot input
# it will also run the do_turn method for us
class MyBot:
    def __init__(self):
        self.logging = True
        
        
    def log_line(self, s):
        if self.logging:
            with open("log.txt", "a") as log:
                log.write(s)
                log.write("\n")
        
    def do_setup(self, ants):
        with open("log.txt", "w") as log:
            log.write(" ")
        self.ants = ants
        self.my_ants = []
        self.destinations = []
        self.unseen = []
        self.my_hills = ants.my_hills()
        for position in ants.my_ants():
            self.my_ants.append(Ant(ants, position, self))
    

    def do_turn(self, ants):
        self.log_line("NEW TURN ---------------------------------:" + str(len(ants.my_ants())) + " - " + str(len(self.my_ants)))
        self.new_positions = []
        #update my_ants
        for position in ants.my_ants():
            ants_i_already_have = set([ant.position for ant in self.my_ants])
            if not position in ants_i_already_have:
                self.my_ants.append(Ant(ants, position, self))
                self.log_line("Ant added")
                
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
        self.state = None
        self.last_position = None

    def clear_state(self):
        try:
            self.bot.destinations.remove(self.destination)
        except Exception, e:
            self.bot.log_line(str(e))

        self.destination = None
        self.distance_to_destination = None
        self.state = None
    

    def update(self):            
        self.bot.log_line("Update:")
        if self.position == self.last_position: 
            self.bot.log_line("SAME POSITION")
            self.clear_state()
            self.move_random()
            
        if self.destination == self.position:
            self.bot.log_line("\tReached destination")
            self.destination = None
        
        if self.state == "Moving to food":
            if not self.destination in self.ants.food():
                self.bot.log_line("\tFood gone, clear state")
                self.clear_state()
                
        if not self.destination:
            self.bot.log_line("\tNo Destination, calculate new order")
            if self.move_to_food(): self.state = "Moving to food"
            else:
                self.move_random() 
                self.state = "Moving random"

        self.move()

    def move_to_food(self):
        self.distance_to_destination, x, self.destination = self.search_for_food()
        if self.destination:
            self.bot.destinations.append(self.destination)
            self.bot.log_line("move_to_food:true")
            return True
        self.bot.log_line("move_to_food:false")
        return False

    def move_random(self):
        self.bot.log_line("move_random")
        directions = {0:'n',1:'e',2:'s',3:'w'}
        random_direction = random.randint(0,3)
        self.bot.log_line(str(random_direction))
        self.destination = self.ants.destination(self.position, directions[random_direction])
        if self.ants.unoccupied(self.destination) and not self.destination in self.bot.new_positions and not self.destination in self.bot.my_hills:
            return True
        else:
            self.move_random()

    def move(self):
        self.last_position = self.position
        direction_to_move = None
        self.bot.log_line("\tMove:")
        for direction in self.ants.direction(self.position, self.destination):
            self.new_position = self.ants.destination(self.position, direction)
            if self.ants.unoccupied(self.new_position) and not self.new_position in self.bot.new_positions and not self.new_position in self.bot.my_hills:
                self.bot.log_line("\t\tDirection ok.")
                self.bot.new_positions.append(self.new_position)
                self.ants.issue_order((self.position, direction))
                self.position = self.new_position
                return
        
            self.bot.log_line("\t\tDirection failed")
        
    def search_for_food(self):
        food_list = []
        
        for food_position in self.ants.food():
            dist = self.ants.distance(self.position, food_position)
            if not food_position in self.bot.destinations:
                food_list.append((dist, self.position, food_position))
        food_list.sort()
        self.bot.log_line(str(food_list))
        if len(food_list) > 0:
            return food_list[0]
        else:
            return (False, False, False)
                
    

    def execute(self):
        if self.order == "move": self.move()

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
