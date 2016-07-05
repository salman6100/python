# nesting dictionary in dictionary

users = { 

        'ssnake':{
        'firstname':' solid',
        'lastname' : ' liquid',
        'game': ' metal gear solid V'
        },



'lsnake':{
'firstname' : 'liquid',
'lastname': 'snake',
'game' : " metal gear solid 4"
},


}

for user, user_info in users.items():
	print("user name : " + user)
	full_name = user_info['firstname'] + " " + user_info ['lastname']
	game = user_info ['game']

	print("The full name of user  is :" + full_name.title())
	print (" game that user is in  " + game.upper())



