# using multiple lists

pizza_toppings = [ 'mushrooms', 'olives', ' green peppers', 'pepperoni', 'chicken']

requested_toppings = [ 'mushrooms', ' olives', ' fries']

for requested_topping in requested_toppings:

	if requested_topping in pizza_toppings:


		 print ( "adding" + requested_topping)


	else:

		print ( "Sorry, we dont have " + requested_topping + " . ")

print ("\nFinished making your pizza")	