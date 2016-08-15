class Clock(object):
    """A clock is initialized to a specific time and can have minutes added or subtracted."""
    
    def __init__(self, hour, minute):
        # roll over hours if greater than 23
        while hour > 23:
            hour -= 24
            
        # roll over minutes if greater than 59
        while minute > 59:
            minute -= 60
            if hour == 23:
                hour = 0;
            else:
                hour += 1
        
        # negative hours
        while hour < 0:
            hour += 24
        
        # negative minutes
        while minute < 0:
            minute += 60
            if hour == 0:
                hour = 23
            else:
                hour -= 1
            
        self.hour = hour
        self.minute = minute
    
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
        # adding minutes
        if quant >= 0:
            self.minute += quant
            while self.minute > 59:
                self.minute -= 60                
                # roll over hours
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
        
        # subtracting minutes
        else:
            self.minute += quant
            while self.minute < 0:
                self.minute += 60
                # roll over hours
                if self.hour == 0:
                    self.hour = 23
                else:
                    self.hour -= 1
       
        return self
        
    def __eq__(self, other):
        """Two clocks set to the same time are equal."""
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False
