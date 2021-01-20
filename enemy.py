from character import Character

'''
Enemy is a subclass of Character
'''
class Enemy:
	'''
	The Constructor should accept the following parameters with these defaults:
		hp = 50
		max_hp = 50
		name = 'Alien'
	
	It should also set the Player's attack_dmg to be 5.
	'''
	def __init__():
    		pass
	
	'''
	This method should receive a parameter that is the object that is the target of the attack.
	Call the hit method for that object and send it the amount of damage caused.
	'''
	def attack():
    		pass
	
	'''
	Print a vengeful message that the Enemy has died.
	'''
	def die():
    		pass
	
	'''
	Receive damage from an attack.  Reduce hp by dmg, print an updated health status, die if out of hp.
	'''
	def hit():
    		pass
			
	'''
	return a message that includes the Enemy's name and health status.
	'''
	def __str__():
    		pass
