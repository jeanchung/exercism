def slices(numbers, n):
    """
    Takes a string of digits and returns all the contiguous 
    substrings of length 'n' in that string.
    """
    run = [int(x) for x in numbers]
    series = []
    
    if n > len(run) or n == 0:
        raise ValueError
    
    i = 0    
    while i + n <= len(run):
        series.append(run[i:i+n])
        i += 1
    
    return series