from player import Player
from enemy import Enemy

spaceman = Player()
print(spaceman)
alien = Enemy()
print(alien)
print()

hero = Player(150, 150, 'Harry Potter')
print(hero)
dementor = Enemy(100, 100, 'Dementor')
print(dementor)

# This should kill the hero
for x in range(50):
	dementor.attack(hero)
print(hero)

hero.heal()
print(hero)

# This should kill the dementor
for x in range(10):
	hero.attack(dementor)
print(dementor)
