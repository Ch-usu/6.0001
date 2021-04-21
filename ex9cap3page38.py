#Add some code to the implementation of Newton-Raphson that
#keeps track of the number of iterations used to find the root. Use that code as
#part of a program that compares the efficiency of Newton-Raphson and bisection
#search. (You should discover that Newton-Raphson is more efficient.)

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
#epsilon = 0.01
#k = 24.0
#guess = k/2.0
#while abs(guess*guess - k) >= epsilon:
 #guess = guess - (((guess**2) - k)/(2*guess))
#print('Square root of', k, 'is about', guess)

#answer:

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
itNewton = 0 
while abs(guess*guess - k) >= epsilon:
    itNewton += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)


#Bisection
itBisection = 0
low = 0.0
high = max(1.0, k)
ans = (high + low)/2.0

while  abs(ans**2 - k) >= epsilon:

    print('low =', low, 'high =',high, 'ans =', ans)
    itBisection += 1 # this is equal to numGuesses = numGuesses + 1
    
    if ans**2 < k:
        low = ans
    
    else:
        high = ans

    ans = (high + low)/2.0

print('numGuesses =', numGuesses)
print(ans, 'is close to square rooot of', k)

#condition

if(itNewton > itBisection):
    print('the most eficient is', itNewton)
else:
    print('the most eficient is', itBisecction)