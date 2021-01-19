from character import Character

'''
Player is a subclass of Character
'''
class Player():
	'''
	The Constructor should accept the following parameters with these defaults:
		hp = 100
		max_hp = 100
		name = 'Spaceman Spiff'
	
	It should also set the Player's attack_dmg to be 5.
	'''
	def __init__(hp, max_hp, name):
		super().__init__(hp, max_hp, name)
		self.hp = 100
		self.max_hp = 100
		self.name = 'Spaceman Spiff'
		self.attack_dmg = 5
	
	'''
	This method should receive a parameter that is the object that is the target of the attack.
	Call the hit method for that object and send it the amount of damage caused.
	'''
	def attack():
		target.hit(self.attack_dmg)
	
	'''
	Print a pithy message that the Player has died.
	'''
	def die(self):
		print(name + " has died.")
	
	'''
	No parameters.  Heal the Player back to maximum health.  Print a message saying that.
	'''
	def heal():
		self.hp = self.max_hp
		print(self + " is fully healed.")
	
	'''
	Receive damage from an attack.  Reduce hp by dmg, print an updated health status, die if out of hp.
	'''
	def hit(self, dmg):
		self.hp -= dmg
		print(self.name + ' has ' + str(self.hp) + '/' + str(self.max_hp) + ' health.')
		if self.hp == 0:
			self.die()
			
	'''
	return a message that includes the Player's name and health status.
	'''
	def __str__(self):
		return 'Player ' + self.name + ' has ' + self.hp + '/' + self.max_hp + ' health.'