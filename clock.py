class Clock(object):
    """
    A clock is initialized to a specific time.
    It can have minutes added or subtracted.
    """

    def __init__(self, hour, minute):            
        self.hour = hour
        self.minute = minute
        self.rollover()
    
    def __str__(self):      
        return "{0:02d}:{1:02d}".format(self.hour, self.minute)
        
    def add(self, quant):
        self.minute += quant
        self.rollover()
        return self
    
    def rollover(self):
        hour_temp, self.minute = divmod(self.minute, 60)
        self.hour = (self.hour + hour_temp) % 24 
        
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
