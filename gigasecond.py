from datetime import timedelta

def add_gigasecond(birthday):
    """
    Given a person's birthday, calculate the date that they turned or will celebrate their 1 gigasecond anniversary.
    
    1 gigasecond = 1 billion seconds
    """ 
    
    gigasecond = timedelta(seconds = 10**9)
    return birthday + gigasecond
