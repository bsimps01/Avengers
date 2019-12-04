#SuperHeroTeamDueler

import random

class Ability:
    #Creates the ability of the charcater
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
        
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Armor:
    #Creates the defense for the character
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value

class Hero:
    def __init__(self, name, starting_health = 100):
#Sets up the current health and starting health of the character
        self.name = name
        self.starting_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

#Adds the ability to the list
    def add_ability(self, ability):
        self.ability = ability
        self.abilities.append(ability)

#Creates the attack method for the character
    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        #adds armor for our characters
        self.armor = armor
        self.armors.append(armor)

    def defend(self, damage_amt):
        #Takes in what the damage does to the character
        blocks = 0
        self.damage_amt = damage_amt
        for blocks in self.armors:
            blocks += damage_amt.block()
            return blocks

    def take_damage(self, damage):
        #Confirms the amount of damage taken
        self.current_health -= damage

    def is_alive(self):
        #Checks if the Hero has health
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        #Logic that checks if the hero and opponent are still standing
        while self.is_alive() and opponent.is_alive():
            if len(self.abilities) > 0 and len(opponent.abilities) == 0:
                opponent.take_damage(self.attack())

            elif len(opponent.abilities) > 0 and len(self.abilities) == 0:
                self.take_damage(opponent.attack())

            else:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
        #Checks to see who is the last person standing in the arguement
        if self.is_alive():
            print(f"{self.name} won!")
            opponent.add_death(1)
            self.add_kill(1)
            
        else:
            print(f"{opponent.name} won!")
            self.add_death(1)
            self.add_kill(1)

    def add_weapon(self, weapon):
        #Adds weapon to abilities list
        self.weapon = weapon
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        #Updates the number of kills
        self.kills += num_kills

    def add_death(self, num_deaths):
        #Updates the number of deaths
        self.deaths += num_deaths

class Weapon(Ability):
    #This method returns a random value between one half to full attack power of the weapon.
    def attack(self):
        return random.randint(0, self.max_damage)

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        #Removes hero from hero list
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            if not foundHero:
                return 0
    
    def view_all_heroes(self):
        #Prints all the heroes to the list
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        #Adds the hero object to the list
        self.heroes.append(hero)

    def stats(self):
        #Prints team statistics
        for hero in self.heroes:
            print("Your Hero: {}".format(hero.name))
            print("Kills/Deaths: {}/{}".format(hero.kills, hero.deaths))

    def revive_heroes(self):
        #Resets all heroes health to starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        #Defines which characters fight who at random if they are alive
        self.other_team = other_team
        living_heroes = list()
        living_opponents = list()
        random_hero = random.choice(self.heroes)
        random_opponent = random.choice(self.other_team.heroes)

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero.fight(random_opponent)
        
    def currently_alive(self):
        #Checks if they are alive
        currently_alive = []
        for hero in self.heroes:
            if hero.is_alive == True:
                currently_alive.append(hero)
            return currently_alive

class Arena:
    def __init__(self):
        #Sets up the teams
        print("\nWelcome to the Champions' Arena where anything is possible!\n")
        self.teamalpha = input("What is the name of the first team?...")
        self.teambravo = input("What is the name of the second team?..")
        self.team_one = Team(self.teamalpha)
        self.team_two = Team(self.teambravo)

    def create_ability(self):
        #States the abilites of the characters
        name = input("What is the ability name?...")
        max_damage = input("What is the max damage of the ability?...")
        return Ability(name, int(max_damage))

    def create_weapon(self):
        #Creates the name of your weapon
        weapon_name = input("Name your weapon...")
        max_damage = input("Max Damage?...")
        return Weapon(weapon_name, int(max_damage))

    def create_armor(self):
        #Adds Armor info to your character
        armor_name = input("Name your armor...")
        armor_block = input("Max armor block: ")
        return Ability(armor_name, int(armor_block))

    def create_hero(self):
        #Make your hero
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("\n[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        #BUilds the first team
        teamalpha = input("How many heroes are in the fight?...")
        #team_one = Team(name)
        if teamalpha != None:
            for _ in range(0, int(teamalpha)):
                hero = self.create_hero()
                self.team_one.add_hero(hero)
        else:
            teamalpha = input("Incorrect Input. Please enter a number: ")
            return teamalpha

    def build_team_two(self):
        #Builds the second team
        teambravo = input("How many heroes in the second squad?...")
        # team_two = Team(name)
        if teambravo != None:
            for _ in range(0, int(teambravo)):
                hero = self.create_hero()
                self.team_two.add_hero(hero)
        else:
            teambravo = input("Incorrect Input. Please enter a number: ")
            return teambravo

    def team_battle(self):
        #Makes both teams fight eachother
        self.team_one.attack(self.team_two)

    def show_stats(self):
        #Prints team statistics to the terminal
        print("\nStats: ")
        self.team_one.stats()
        self.team_two.stats()

        if len(self.team_one.currently_alive()) > 0:
            print(self.team_one + "wins")
        else:
            print(self.team_two + "wins")

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