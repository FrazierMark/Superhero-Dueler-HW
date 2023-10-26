from random import choice, random
from ability import Ability
from armor import Armor

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
        
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        
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



if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)