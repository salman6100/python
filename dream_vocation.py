dream_vocation = {}

dream_vocation  = True

while dream_vocation:
	
	
		
	dream_vocation = input(" Tell me a place you would love to visit :  ")
	
	vocations = dream_vocation
	
	
	repeat = input(" If anybody likes to say their favorite vocation spot:")
	
	if repeat == 'no':
		
		dream_vocation = False
	
	for  vocations in dream_vocation:
	
		print(" you picked " + dream_vocation + " . ")
		
		