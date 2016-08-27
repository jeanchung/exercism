def square_of_sum(n):
    """Calculates the square of the sum of the first n natural numbers."""
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum * sum

def sum_of_squares(n):
    """Calculaes the square of the sum of the first n natural numbers."""
    sum = 0
    for i in range(1, n+1):
        sum += i * i
    return sum

def difference(n):
    """Calculates the difference between the results of above two functions."""
    return square_of_sum(n) - sum_of_squares(n)
