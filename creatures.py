#===================================
# this is a class which can hold the 
# skill, luck and stamina of
# the player, and also of monsters
#===================================
class creature:
	def __init__(self, name, skill, stamina, luck):
		self.skill = skill
		self.stamina = stamina

		self.name = name
	
	def PrintStatus(self):
		print("Status for " ,self.name + " is as follows:")
		print("    Skill: " , self.skill)
		print("    Stamina: " , self.stamina)


class human:
	def __init__(self, name, skill, stamina, luck):
		self.skill = skill
		self.stamina = stamina
		self.luck = luck
		self.name = name
	
	def PrintStatus(self):
		print("Status for " ,self.name + " is as follows:")
		print("    Skill: " , self.skill)
		print("    Stamina: " , self.stamina)
		print("    Luck: ", self.luck)
