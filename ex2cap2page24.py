#Replace the comment in the following code with a while loop
#numXs = int(input("how many times should i print the letter X"))
#concatenate X to toPrint numXs times
# print(toPrint)

numXs = int(input("how many times should i print the letter X"))

iterations = numXs

toPrint = ""

while(iterations != 0):

    toPrint = toPrint + "X"
    iterations = iterations - 1


print(toPrint)