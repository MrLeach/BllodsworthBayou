#=====================================
# This file contains all the locations
# programmed by Bob
#=====================================
from creatures import *

# here is an example of a battle
def location2(player):
	ClearScreen()
	print("""
Unfortunately, there is a very big tortoise here, 
and there is no choice but to fight it
""")

	demon = creature("Demonic Tortoise",20,20,10)
	fight(player, demon)
	if player.stamina <= 0:
		print("You lost to the tortoise")
		return 0
	else:
		print("Yay! Tortoise soup tonight!")
		return 3

