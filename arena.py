from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena(Team):
    def __init__(self, team_one = None, team_two = None):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
    
        self.team_one = team_one
        self.team_two = team_two
        
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        
        ability_name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(ability_name, int(max_damage))
    
    def create_weapon(self):
        '''Prompt user for Weapon information
        return Weapon with values from user input
        '''
        
        weapon_name = input("What is the weapon name?  ")
        max_damage = input("What is the max damage of the weapon?  ")
        return Weapon(weapon_name, int(max_damage))
    
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        
        armor_name = input("What is the armor name?  ")
        max_block = input("What is the max block of the armor?  ")
        return Armor(armor_name, int(max_block))
    
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        
        hero_name = input("What is the hero name?  ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero
    
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        
        if self.team_one == None:
            team_name = input("What is the name of team one?  ")
            self.team_one = Team(team_name)
            
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        
        if self.team_two == None:
            team_name = input("What is the name of team two?  ")
            self.team_two = Team(team_name)
        
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        
        team1_kills = 0
        team1_deaths = 0
        for hero in self.team_one.heroes:
            team1_kills += hero.kills
            team1_deaths += hero.deaths
        if team1_deaths == 0:
            team1_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team1_kills/team1_deaths))
        
        
        team2_kills = 0
        team2_deaths = 0
        for hero in self.team_two.heroes:
            team2_kills += hero.kills
            team2_deaths += hero.deaths
        if team2_deaths == 0:
            team2_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team2_kills/team2_deaths))
        
        
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
                
                
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

        
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()