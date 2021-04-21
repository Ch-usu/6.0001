#write a program that asks the user to enter an integer and prints two integers, root
#and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
#if not such pair of integers exists, it should print a message to that effect


number = int(input("insert an integer "))

root = 1
pwr = 1

while(pwr < 6):

    multiply = root**pwr 

    if(multiply == number):

        print("the power is: ", pwr, "the root is:", root)
        break
    else:
        print(root)
        print(pwr)
        root = root + 1

    if(root == 6):

        print(root)
        print(pwr)
        root = 1
        pwr = pwr + 1

if(multiply != number):

    print("there is not a power and a root that equals the number you entered")
     