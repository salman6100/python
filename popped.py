moto = [ 'honda', ' yamah', ' suzuki']
print( moto)

popped_moto = moto.pop()
print ( moto)
print ( popped_moto)


last_owned = popped_moto

print(" The last moto i bought was" +  last_owned.upper())

first_owned = moto.pop(1)

print ( " The first owned moto was "+ first_owned.title() + '.')

print ( moto)

moto.append('yamah')
moto.append (' ducati')

print ( moto)

moto.remove('honda')
print(moto)


moto.append ( 'honda')

print ( moto)

moto.append( 'suzuki')
print( moto)


exp= 'honda'
moto.remove(exp)
print(moto)

print( "\nA" + ' '+ exp.title() + " is too expensive for me.")


