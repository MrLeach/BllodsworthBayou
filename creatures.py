#===================================
# this is a class which can hold the 
# skill, luck and stamina of
# the player, and also of monsters
#===================================
class creature:
	def __init__(self, name, skill, stamina):
		self.skill = skill
		self.stamina = stamina
		self.name = name
	
	def PrintStatus(self):
		print("Status for " ,self.name + " is as follows:")
		print("    Skill: " , self.skill)
		print("    Stamina: " , self.stamina)


class human:
	def __init__(self, name, skill, stamina, luck, fear):
		self.skill = skill
		self.stamina = stamina
		self.luck = luck
		self.name = name
		self.fear = fear
		
		self.max_skill = skill
		self.max_stamina = stamina
		self.max_luck = luck
		self.max_name = name
		self.max_fear = fear
		
	
	def PrintStatus(self):
		print("Status for " ,self.name + " is as follows:")
		print("    Skill: " , self.skill, "Max: ", self.max_skill)
		print("    Stamina: " , self.stamina, "Max: ", self.max_stamina)
		print("    Luck: ", self.luck, "Max: ", self.max_luck)
		print("    Luck: ", self.fear, "Max: ", self.max_fear)
