def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        fact = 1
        for i in range(2, x+1):
            fact *= i
        return fact
    
print(factorial(5))