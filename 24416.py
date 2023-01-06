n = int(input())

def fib(n):
    if n==1 or n==2:        
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    f = [1] * n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f[n-1]

print(fibonacci(n),n-2)