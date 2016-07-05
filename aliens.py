# multiple dictionaries ( nested) 

# empty list of aliens
aliens =[]

# make 50 red aliens

for alien_num in range(50):

	new_alien = { 'color' : 'red' , 'points': 7, 'size': 'round'}

	aliens.append(new_alien)

# show first 10 aliens

for alien in aliens[:10]:
	print(alien)

print (".....")




	# show how many aliens have been created

print ( "Total number of aliens" + str(len(aliens)))


