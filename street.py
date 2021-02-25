class Street:
    def __init__(self, name, length, start, end, cars=[], is_green=False):
        self.length = length
        self.start = start
        self.end = end
        self.name = name
        self.length = length
        self.cars = cars
        self.is_green = False
        
    def __repr__(self):
        return f"Street {self.name} - (Start: {self.start}, End: {self.end}, Length: {self.length})."
