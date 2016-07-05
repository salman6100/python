nba = {
	
	'knicks' :{

	'playera' : ' anthony',
	'playerb'  : 'porzingha',
	'playerc'   : ' drant',
},


}

for player, team_players in nba.items():
	print(player + " :=")

teamknicks = team_players['playera'] + " " + team_players ['playerb'] + team_players['playerc']

print("The following knicks team players are : " + teamknicks)



	