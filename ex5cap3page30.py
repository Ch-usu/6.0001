#let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. write a program 
#that prints the sum of the numbers in s

s = '1.23,2.4,3.123'
number = ''
i = 0 
sum = 0
for letter in s:
    
    
    number = str(number) + str(letter)
    print(number)

    if(letter == ','):

        sum = sum + float(number[0:-1])
        print(sum)
        number = ''
    
    if(i == (len(s) - 1)):
    
        sum = sum + float(number)

    i = i + 1
    
print("the sum of the string is: ", sum )
   