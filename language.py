programming = { 
'jen':'c',


 'sarah' :'python',
  'edward':    'c++',
   'phil' :   'java',



      }

for name, langs in programming.items():

 print(name.title()  + " favorite programming languages is " + langs + " .")
# using if state ment 
if 'Jack' not in programming:
	print( " Jack , please take our poll!""\n")

# looping in dictionary in order

for name in sorted (programming):
	print(name.title() + " thank you for taking the poll.""\n")

# looping through whole dic
for langs in programming.values():
	print (langs)

# looping without repeating

for langs in  set ( programming.values()):

	print ( langs)

		
