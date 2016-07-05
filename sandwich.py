sandwich_orders = [' chicken sandwich', ' beef sandwich', ' veg sandwich', 'egg sandwich']


finished_sandwiches = []


while sandwich_orders :
	
	 sandwich = sandwich_orders.pop()
	
	
	 print(" I made you " +  str (sandwich) + " . ")
	 finished_sandwiches.append(sandwich)
	
	
	
	#display completed sandwich
	
	
	print("\nAll following sandwich are made :")
	
	for sandwichs in finished_sandwiches:
		
		print(sandwichs)
	     
	
	