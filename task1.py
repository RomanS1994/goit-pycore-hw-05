def caching_fibonacci():
    cash = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cash:
            return cash[n]
        else:
            cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
            # print(cash)
            return cash[n]
    
    return fibonacci
    

fib = caching_fibonacci()


print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

