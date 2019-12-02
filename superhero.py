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
        self.armor = armor
        self.armors.append(armor)

    #def defend(self, damage_amt):

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())