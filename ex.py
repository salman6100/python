destination = {}

travel_active = True

while travel_active:
	
	
	name = input(" Can you please tell me your name :")
	
	location = input(" where would you like to travel :")
	
	
	destination [ name ] = location
	
	
	repeat = input(" Is any body else wants to travel")
	
		
	if repeat == 'no':
		
		 travel_active = False
		
		
		# result
		
	print ( " \nThe result is :")
		
	for name , location in destination.items():
			
		print ( name + " would like to go to =>" + location + " .")


    	
	
	
	
	