from player import Player
from enemy import Enemy

def testPlayerDefaultConstructor():
  p = Player()
  assert p.hp == 100, 'Incorrect default for Player.hp'
  assert p.max_hp == 100, 'Incorrect default for Player.max_hp'
  assert p.name == 'Spaceman Spiff', 'Incorrect default for Player.name'
  assert p.attack_dmg == 5, 'Incorrect default for Player.attack_dmg'

def testEnemyDefaultConstructor():
  p = Enemy()
  assert p.hp == 50, 'Incorrect default for Enemy.hp'
  assert p.max_hp == 50, 'Incorrect default for Enemy.max_hp'
  assert p.name == 'Alien', 'Incorrect default for Enemy.name'
  assert p.attack_dmg == 3, 'Incorrect default for Enemy.attack_dmg'

def testPlayerConstructor():
  p = Player(200, 200, "Max")
  assert p.hp == 200, 'Incorrect value for Player.hp'
  assert p.max_hp == 200, 'Incorrect value for Player.max_hp'
  assert p.name == 'Max', 'Incorrect value for Player.name'
  assert p.attack_dmg == 5, 'Incorrect value for Player.attack_dmg'

def testEnemyConstructor():
  p = Enemy(200, 200, "Max")
  assert p.hp == 200, 'Incorrect value for Enemy.hp'
  assert p.max_hp == 200, 'Incorrect value for Enemy.max_hp'
  assert p.name == 'Max', 'Incorrect value for Enemy.name'
  assert p.attack_dmg == 3, 'Incorrect value for Enemy.attack_dmg'

def testPlayerAttack():
  p = Player(100,100,'P')
  e = Enemy(50,50,'E')
  p.attack(e)
  assert e.hp == 45, 'Incorrect value for Enemy.hp after attack by Player'

def testEnemyAttack():
  p = Player(100,100,'P')
  e = Enemy(50,50,'E')
  e.attack(p)
  assert p.hp == 97, 'Incorrect value for Player.hp after attack by Enemy'

def testPlayerHeal():
  p = Player(100, 100, 'P')
  e = Enemy(50, 50, 'E')
  e.attack_dmg = 100
  e.attack(p)
  p.heal()
  assert p.hp == p.max_hp, 'Incorrect value for Player.hp after healing'

