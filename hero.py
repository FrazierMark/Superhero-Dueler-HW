from random import choice, random
from ability import Ability
from armor import Armor
from weapon import Weapon

# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  
  
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''

        self.abilities = list()
        self.armors = list()
        
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        
        
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''
        
        total_power = self.starting_health + opponent.starting_health
        hero_chance = self.starting_health / total_power
        oop_chance = opponent.starting_health / total_power
        
        
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                if random() <= hero_chance:
                    opponent.take_damage(self.attack())
                else:
                    self.take_damage(opponent.attack())
            if self.is_alive():
                print(f"{self.name} won!")
            else:
                print(f"{opponent.name} won!")
                
        
    
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        
    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        
        self.armors.append(armor)
        
    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
         # TODO: This method should run the block method on each armor in self.armors
        total_block = 0
        if len(self.armors) > 0 and self.current_health > 0:
            for armor in self.armors:
                total_block += armor.block()
        return total_block
    

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        total_damage = damage - self.defend()
        total_damage = max(total_damage, 0)
        self.current_health -= total_damage
        
    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())