class Street:
    def __init__(self, name, length, start, end, is_green=False):
        self.light = TrafficLight()
        self.name = name
        self.length = length # == Time
        self.start = start
        self.end = end
        self.is_green = False
        self.cars = []

    def __repr__(self):
        return f"Street {self.name} - (Start: {self.start}, End: {self.end}, Length: {self.length})"

class TrafficLight:

    COLOURS = ['RED', 'GREEN']

    def __init__(self):
        # red by default
        self.colour = 'RED'

    def __bool__(self):
        """ Return true if we can go! """
        return self.colour == 'GREEN'

    def setRed(self):
        self.colour = 'RED'

    def setGreen(self):
        self.colour = 'GREEN'

    def change(self):
        """ change from one state to the other """
        self.colour = 'GREEN' if self.colour == 'RED' else 'RED'