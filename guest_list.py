# this program create lists, add , remove and del from lists

list = [ 'tariq', ' farooq', ' shariq']
message = " would you like to come to dinner today?."

print ( message + list[0].title())
print ( list[1].title() + message)
print ( message.title() + list[2].upper())


cannot_makeit = 'tariq'
list.remove(cannot_makeit)
print(list)
print ("The follow guest"+" " + cannot_makeit.title() + " will not make it to dinner")

list.insert ( 0, ' Jamal')
print( list)
print ( message + list[0])
print( list[1].title() + message.title())
print ( message.title() +  list[2].upper())

print ( " \n I found a bigger table so more guests are invited")


list.insert (0, ' jack')
list.insert ( 3, 'ironman')
list.insert (5, ' cena')

print (list)

msg = " Hello , please come to dinner today at 8 pm, thank you!"
print ("\n")
print (msg + list[0].upper())
print ("\n" + msg + list[1])
print ( "\n\t" + list[2].title() + msg.title())

print ( "\t\t" + list[3].title() + " and " + list [4].title() + msg.upper())

print ( msg + list [5].title())

print ( " due to not available dinner table there is only capacity only two guest ")

guest_remove = list.pop(0)
print ( guest_remove + " Sorry there is no room on the dinner table.")

guest_remove = list.pop(1)
print( guest_remove + " sorry next time.")
print ("\n" + str(list))

guest_remove = list.pop(2)
print ( guest_remove.upper() + " Next time ")
print (list)

guest_remove = list.pop(0)
print (list)


print ( guest_remove + " Good Bye")

print ( list)

msg2 = " You are still invited to dinner."
print( list[0] + " haha, you are on for dinner tonight")
print ( list[1].upper() + msg2.upper())


print ("\t\t\t\n" + str(list))

del list
print ( list)
print(list)








