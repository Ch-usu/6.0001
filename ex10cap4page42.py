#Write a function isIn that accepts two strings as arguments and
#returns True if either string occurs anywhere in the other, and False otherwise.
#Hint: you might want to use the built-in str operation in.

#If string1 is in string2 it is clear that string2 is in string1

def isIn(string1, string2): 
    if(string1 in string2):
        return True, print('True')
    else:
        return False, print('False')


isIn('hola', 'ho')
    