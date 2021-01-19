'''
This is the class that will be used for every character type in a game.
This class is written correctly.  
Use this class to help setup the Player class and the Enemy class.
'''
class Character:
	def __init__(self, hp=0, max_hp=0, name=''):
		self.hp = hp
		self.max_hp = max_hp
		self.name = name
		
	def __str__(self):
		return "This generic Character is named " + self.name + " and has " + str(self.hp) + "/" + str(max_hp) + " hit points."
