prompt = "\nPlease tell me your age:"

while True:
	
	age = input ( prompt)
	
	if age == 'quit':
		
		 	break
		
		
						
	elif int(age ) <=3 :
		
			print ( " your ticket  is $5")
		
	elif int ( age ) <=10:
		
			print ( " your ticket is $10")	
			
	else:
		
			print ( " You ticket is $20")		
	
	