from alice import *
from bob import *
from carol import *
import random
from creatures import *
import builtins
import os


#===================================
# start the game by making a global
# variable for the player's stauts
#===================================
player = human("Playername", 10, 20, 3)
player.PrintStatus()

#===========================================================
# this is the fighting function. It has two PARAMETERS
# parameter 1 is the status of the player
# parameter 2 is the status of the monster
#==========================================================
def fight(player, monster):
	print("There is going to be a battle")
	player.PrintStatus()
	monster.PrintStatus()
	
	# TO DO - replace this with your fighting 
	# code, but your skill would be 'player.skill'
	# the monster's skill would be 'monster.skill'
	# and so on 
	
	result = random.randint(0,1)
	if result == 0:
		player.stamina = 0
	else:
		monster.stamina = 0
#======== End of fight function =========================


# make this available to all modules (don't worry about this...)
builtins.fight = fight

def ClearScreen():
	os.system("clear") # unix
	os.system("cls")   #windows
builtins.ClearScreen = ClearScreen


#=================================================================
# main loop of the program
# currentLocation is the part we are on
# nexLocation is the number (from the book) of the place to go next
# currentFunction is name of the function which someone should have 
# made to deal with the part we are on.
# lastLocation is the last place we went where the code worked
#
# The functions which you write have to return the number of the 
# section of the book which the player should visit next
#
# Basically, don't worry about how this works until much
# later in the course
#
#=================================================================
currentLocation = 1
nextLocation = 1
lastLocation = 1
while player.stamina > 0:
	try:
		# move the current location to the next 
		currentLocation = nextLocation
		currentFunction = "location" + str(currentLocation) + "(player)"
		input("You are now going to location"+ str(currentLocation)+"\nPress ENTER to go there") 
		nextLocation = eval(currentFunction);
		# last location that worked
		lastLocation = currentLocation
	except Exception as e:
		print("Error, there was a problem with function", str(currentFunction), "\nThe error message was: ", str(e))
		input("Press ENTER to go back to location" + str(lastLocation))
		nextLocation = lastLocation


# if you get here, stamina is <= 0
print("So sorry, that is the end of the game")
