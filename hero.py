from random import choice, random

# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  
  
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        
        
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''
        
        total_power = self.starting_health + opponent.starting_health
        hero_chance = self.starting_health / total_power
        oop_chance = opponent.starting_health / total_power
        
        if random() < hero_chance:
            winner = self
            loser = opponent 
        else: 
            winner = opponent
            loser = self
        
        print(f"{winner.name} defeats {loser.name}! {winner.name} wins!")
        


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    hero1.fight(hero2)