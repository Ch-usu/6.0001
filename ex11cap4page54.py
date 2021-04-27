#Finger exercise: When the implementation of fib in Figure 4.7 is used to compute
#fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)?

#the code is the following

#def fib(n):
# """Assumes n int >= 0
# Returns Fibonacci of n"""
# if n == 0 or n == 1:
# return 1
# else:
# return fib(n-1) + fib(n-2)
#def testFib(n):
# for i in range(n+1):
# print('fib of', i, '=', fib(i))

#for this what i do is the following:

#   fib(5) = fib(4) + fib(3)
#   fib(5) = fib(3) + fib(2) + fib(2) + fib(1)
#   fib(5) = fib(2) + fib(1) + fib(2) + fib(2) + fib(1)

#   with this ecuation we can easily see that fib(2) is repeated 3 times