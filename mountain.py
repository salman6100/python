iceskating = {}

skating_active = True

while skating_active:
	
	# Asker user their name
	
	name = input(" What is your name :")
	
	iceskatings = input ( " where would you like to iceskate : ")
	
	iceskating[name] = iceskatings
	
	repeat = input(" would like to go swimming instead ? ( yes /no )")
	
	if repeat == 'no' :
		
		skating_active = False
		
		
		
		# result 
		
		print ("\n --- Poll Result ---")
		
		for name, iceskatings in iceskating.items():
			
			print(name + " would you like to skate" + iceskatings + " .")
	
	