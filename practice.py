prompt = " Enter a number :"
prompt += " The number has to be even :  "

active  = True

while active:
	
	num = input(prompt)
	
	num = num % 2 == 0
	 
	
	if num != num:
	
		active = False
	
	else:
		
		print (" That is correct :" + str (num) )