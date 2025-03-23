def caching_fibonacci():
    """It creates and uses a cache to store and reuse already computed Fibonacci numbers."""
    cache = {} # Create an empty dictionary to store computed Fibonacci numbers
    
    def fibonacci(n):
        # Check if the result for n is already in the cache
        if n in cache:
            return cache[n]
        
        elif n <= 0: #check if the value n = or < 0 add this value to the dictionary cache
            cache[n] = 0
            return cache[n]
        
        elif n == 1:
            cache[n] = 1
            return cache[n]
        
        # If the value for n hasn't been computed yet, recursively calculate it
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

         # Return the computed result for fibonacci(n)
        return cache[n]
    
    # Return the fibonacci function to allow calling it outside
    return fibonacci


if __name__ == "__main__": 
    # Get the fibonacci function
    fib = caching_fibonacci()

    # Use the fibonacci function to compute Fibonacci numbers
    print(fib(10))  #  55
    print(fib(15))  #  610

            