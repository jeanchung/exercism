NORTH = (0,1)
EAST = (1,0)
SOUTH = (0,-1)
WEST = (-1,0)

class Robot(object):
    """
    A robot has three possible movements:

    - turn right
    - turn left
    - advance

    Robots are placed on a hypothetical infinite grid, facing a particular
    direction (north, east, south, or west) at a set of {x,y} coordinates,
    e.g., {3,8}, with coordinates increasing to the north and east.
    """

    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        
    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = NORTH
    
    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == WEST:
            self.x -= 1
        self.coordinates = (self.x, self.y)
        
    def simulate(self, instructions):
        for letter in instructions:
            if letter == "L":
                self.turn_left()
            elif letter == "R":
                self.turn_right()
            elif letter == "A":
                self.advance()