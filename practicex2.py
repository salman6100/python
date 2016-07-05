prompt = " please enter odd number. ".title()

prompt += " \n only odd number is accepted. ".title()

prompt += " \n if your input is even number  you will not get candy.".title()

print ( prompt)




active = True

while active:
	
	even = input (  )

		
	if even % 2 != 0:
	
		print ( " The number you entered is not even")
	
	else:
		
		print ( " This number is even : "  + str(even))
