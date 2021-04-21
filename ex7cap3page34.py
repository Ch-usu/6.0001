#figure 3.4

#x = -25
#epsilon = 0.01
#numGuesses = 0
#low = 0.0
#high = max(1.0, x)
#ans = (high + low)/2.0

#while  abs(ans**2 - x) >= epsilon:

#    print('low =', low, 'high =',high, 'ans =', ans)
#    numGuesses += 1 # this is equal to numGuesses = numGuesses + 1
    
#    if ans**2 < x:
#        low = ans**2
#    else:
#        high = ans

#    ans = (high + low)/2.0

#print('numGuesses =', numGuesses)
#print(ans, 'is close to square rooot of', x)


#what would have to be changed to make the code in figure 3.4 work 
#for finding an approximation to the cube root of both negative and 
#positive numbers?  (hint: think about changing low to ensure that the
#  answer lies within the region being searched 

x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low)/2.0

while  abs(ans**2 - abs(x)) >= epsilon:

    print('low =', low, 'high =',high, 'ans =', ans)
    numGuesses += 1 # this is equal to numGuesses = numGuesses + 1
    
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans

    ans = (high + low)/2.0

print('numGuesses =', numGuesses)

if(x < 0 ):

    print("i",ans, "is close to square root ", x)    

else:

    print(ans, 'is close to square rooot of', x)

#The hint on this finguer excersise is to change the value of low 
#this hint probably comes from that if we leave the code as it is 
#in figure 3.4 the condition ans**2 < x will never be met
#this means that low will always be cero, that is one the reasons 
#we will never get out of the whiles