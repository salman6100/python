questions ={}

# set ice skating is active.

iceskating_active = True

while iceskating_active:
	
	
	#prompt user for name
	
	name = input("\nwhat is your name : ")
	
	question = input(" where would you like to ice skate")
	
	#store the question in dictionary
	
	questions[name] = question
	
	
	repeat = input(" would you like someelse respond? ( yes/no)")
	
	if repeat == 'no':
		
		iceskating_active = False
		
		print("\n  outcome ")
	
	for name, question in questions.items():
		
		print( name + " would you like to skate"  + question + " .")	
		
		