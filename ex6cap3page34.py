#what would the code in figure 3.4 do if the stateent x = 25
#were replacced by x = -25

#figure 3.4

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while  abs(ans**2 - x) >= epsilon:

    print('low =', low, 'high =',high, 'ans =', ans)
    numGuesses += 1 # this is equal to numGuesses = numGuesses + 1
    
    if ans**2 < x:
        low = ans
    
    else:
        high = ans

    ans = (high + low)/2.0

print('numGuesses =', numGuesses)
print(ans, 'is close to square rooot of', x)

#First of all this program was made to find the square root of a non negative number
#Also a square root mathematically makes no sense unleast we work with imaginaries
#so with this two arguments we can espect in the program to be some kind of failure

#Looking at the code
#the first ans will be ans = 0.5 so in the itterations ans**2 will tend to cero
#this means that the decrementing function will not decrement so, we will have 
#the decrementing function => abs(ans**2 - x) = 25