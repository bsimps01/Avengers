#SuperHeroTeamDueler

import random

class Ability:
    #Creates the ability of the charcater
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
        attack_strength = 100

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Armor:
    #Creates the defense for the character
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
        max_block = 100

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
        self.opponent = opponent
        while self.is_alive() and self.opponent.is_alive():
            if len(self.abilities) > 0 and len(self.opponent.abilities) == 0:
                self.opponent.take_damage(self.attack())
            elif len(self.opponent.abilities) > 0 and len(self.abilities) == 0:
                self.take_damage(self.opponent.attack())
            else:
                self.take_damage(self.opponent.attack())
                self.opponent.take_damage(self.attack())
        #Checks to see who is the last person standing in the arguement
        if self.is_alive():
            print(f"{self.name} won!")
            
        else:
            print(f"{self.opponent.name} won!")

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