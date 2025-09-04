def caching_fibonacci() -> function:
    """
    a function that creates and uses a cache
    to store and reuse already calculated
    Fibonacci number values.
    """

    # create an empty dictionary
    cache = {}

    def fibonacci(n: int) -> int:
        """
        internal function for recursive calculation of Fibonacci numbers
        """

        # block of checks for processing logic
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # return a function with a deferred call to create a closure
    return fibonacci


# assign a function call to a variable
fib = caching_fibonacci()


print(fib(10))
print(fib(15))
