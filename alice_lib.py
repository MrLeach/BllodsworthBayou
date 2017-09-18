#=====================================
# This file contains all the locations
# programmed by Alice
#=====================================
from creatures import *

def location1(playerStatus):
	ClearScreen()
	print("This is the start of the story")
	print("There will be the introductory text here")
	while True:
		choice = input("Go to location 2 or 3?")
		if choice == "2":
			return 2
		elif choice == "3":
			return 3
		else:
			print("please enter 2 or 3")
