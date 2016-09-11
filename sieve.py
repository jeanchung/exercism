def sieve(n):
    """
    Uses the Sieve of Eratosthenes to find all the primes up to a given number "n".
    """
    result = {}
    primes = []
    numbers = range(2, n + 1)
    for i in numbers:
        result[i] = True
    
    while 0 < len(numbers):
        for i in numbers[1:]:
            if i % numbers[0] == 0:
                result[i] = False
        numbers = numbers[1:]
    
    for num in result.keys():
        if result[num] == True:
            primes.append(num)
    
    return primes