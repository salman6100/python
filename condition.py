prompt = " what is your first name:"

prompt += " what city do you live in = >"

active = True

while active:
	
	ans = input ( prompt )
	
	if ans == 'quit':
	
		active = False
	
	else :
		
		print ( ans)
	
	
	