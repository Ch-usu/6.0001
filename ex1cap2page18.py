# Write a program that examines three variables - x,y,z and prints
# the largest odd number among them. if none of them are odd, it should
#print a message to that effect ><


x = int(input("inserte numero x"))
y = int(input("inserte numero y"))
z = int(input("inserte numero z"))

perX = x%2
perY = x%2
perZ = x%2


if( perX != 0 and perY != 0 and perZ != 0):

    if( x > y and  x > z):

        print("el numero impar mas grande es:", x)

    elif( y > z  and y > x ):

        print("el numero impar mas grande es:", y)

    else: 

        print("el numero impar mas grande es:", z)

elif(perY != 0 and perZ != 0):

    if( y > z):

        print("el numero impar mas grande es:", y)

    else: 

        print("el numero impar mas grande es:", z)

elif(perY != 0 and perX != 0):

    if( x > y):

        print("el numero impar mas grande es:", x)

    else: 

        print("el numero impar mas grande es:", y)

elif(perX != 0 and perZ != 0):

    if( x > z):

        print("el numero impar mas grande es:", x)

    else: 

        print("el numero impar mas grande es:", z)

else: 

    print("Los numeros ingresados no son impares")


