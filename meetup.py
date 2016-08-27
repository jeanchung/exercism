from datetime import date
from calendar import monthrange

class MeetupDayException(Exception):
    """Exception raised when date does not exist."""
    pass
    
def meetup_day(year, month, day, number):
    """
    Calculates the date of a meetup.
    
    "number" qualifies "day" and can be an ordinal (e.g. "1st", "last") or "teenth," meaning the date on which that day of the week ends in "teenth."
    """
    
    day_code = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    first_day = date(year, month, 1).weekday()
    input_day = day_code[day] # translate day to int representation
    difference = (input_day - first_day + 7) % 7
        
    if number == "1st" or number == "first":
        result_date = 1 + difference
        return date(year, month, result_date)
        
    elif number == "2nd" or number == "second":
        result_date = 8 + difference
        return date(year, month, result_date)

    elif number == "3rd" or number == "third":
        result_date = 15 + difference
        return date(year, month, result_date)

    elif number == "4th" or number == "fourth":
        result_date = 22 + difference
        return date(year, month, result_date)
    
    elif number == "5th" or number == "fifth":
        result_date = 29 + difference
        try:
            return date(year, month, result_date)
        except:
            raise MeetupDayException("This date does not exist.")
    
    elif number == "teenth":
        if difference > 4:
            result_date = 8 + difference
        else:
            result_date = 15 + difference
        return date(year, month, result_date)
    
    elif number == "last":
        last_date = monthrange(year, month)[1]
        last_day = date(year, month, last_date).weekday()
        difference = (last_day - input_day + 7) % 7
        result_date = last_date - difference
        return date(year, month, result_date)

