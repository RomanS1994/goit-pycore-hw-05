def caching_fibonacci():
    '''
    Creates a function to compute Fibonacci numbers using caching.

    Returns: 
    the fibonacci(n) function, which calculates the nth Fibonacci number.
    '''
    cash = {}
    def fibonacci(n):
        '''
        Computes the n-th Fibonacci number using recursion and caching.

        Parameters:  n (int): 

        Returns: int: The n-th Fibonacci number.
        '''
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


# print(fib(10))  # Виведе 55
# print(fib(15))  # Виведе 610

