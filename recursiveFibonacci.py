def fibonacci(n):
    """Asume a n como int n>=0
    devuelve el numero Fibonacci en
    la posición n"""
    if(n==1 or n==0):
        return 1        
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))