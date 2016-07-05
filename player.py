players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players [ 0 : 2])
print( players [ 0: 3])
print (players[0:4])

players.append(" Ali")
print(players)
print(players[1:5] )

players.append(" jackson")
print(players)

for player in players [:5]:
	print(player.title())


for player in players [ : 5]:
	print(player.upper())