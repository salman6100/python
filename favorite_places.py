favorite_places = {
	
	'salman': [ 'Spain'],
	'Jack': [ 'China'],
	'Jill' : [' England'],
	'Bill': ['Washington DC'],
	'Kelly': ['LA'],


}

for name, places in favorite_places.items() :
	print(name.title()+ " 's favorite  place is :" )

	for place in places:
		print(place.title())