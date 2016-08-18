class Clock(object):
    """A clock is initialized to a specific time.
    It can have minutes added or subtracted."""

    def __init__(self, hour, minute):            
        self.hour = hour
        self.minute = minute
        self.rollover()
    
    def __str__(self):
        # hours are always double digits
        if self.hour < 10:
            displayHour = "0{0}".format(self.hour)
        else:
            displayHour = str(self.hour)
        
        # minutes are always double digits    
        if self.minute < 10:
            displayMinute = "0{0}".format(self.minute)
        else:
            displayMinute = str(self.minute)
            
        return displayHour + ":" + displayMinute
        
    def add(self, quant):
        self.minute += quant
        self.rollover()
        return self
    
    def rollover(self):
        if self.minute < 0:
            multiples = int(self.minute / 60.0) - 1
        else:
            multiples = int(self.minute / 60.0)
    
        self.minute = self.minute % 60        
        self.hour += multiples    
        self.hour = self.hour % 24
        
    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False
