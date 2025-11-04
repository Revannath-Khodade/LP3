def fibonacci(n):
    steps = 0

    if n==0:
        steps = steps + 1
        return 0, steps 
    
    elif n==1:
        steps = steps + 1
        return 1, steps
    
    a=0
    b=1
    steps = steps + 2
    print(a, b, end=" ")

    for i in range(2, n+1):
        c = a+b
        a, b=b, c
        steps = steps + 3
        print(b, end=" ")

    print()
    return b, steps

n= int(input("Enter n: "))

if n<0:
    print("please enter a non-negative number!")
else:
    fib, step_count = fibonacci(n)
    print("Fibonacci(", n, "): ",fib)
    print("Total Steps =",step_count)
