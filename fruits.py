# nested dictionary

fruits = []

# range of fruits we want is 20

for types in range(20):

	new_fruits = { 'shape': 'round', 'fruit' : 'apple', 'cost' : 5}
	fruits.append(new_fruits)


for fruit in fruits [0:3]:

	if fruit ['shape'] == 'round':
		fruit ['shape'] = ' oval'
		fruit ['cost'] = 10


	# show the first 5 frutis:


for fruit in fruits[:5]:
		print(fruit)

print("====")


# how many frutis did we created

print ( " Total number of fruits we created are " + str ( len(fruits)) + ".")



