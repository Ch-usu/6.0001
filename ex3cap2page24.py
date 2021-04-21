#Write a program that asks the user to input 10 integers, and then prints 
#the largest odd number that was entered. If no odd number wa entered it should
#print a message to that effect


mayor = 0
x = 0   

while(True):

    numero = int(input("ingrese un numero "))

    
    if(numero%2 != 0):

        if(numero > mayor):

            mayor = numero

    x = x + 1

    if(x == 10):


        if(mayor != 0):
            
            print("el mayor numero impar es", mayor)
            break
        
        else:

            print("no hay numeros imp")
            break