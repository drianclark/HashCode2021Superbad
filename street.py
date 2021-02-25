class Street:
    def __init__(self, start, end, name, length, cars=[], lights=[]):
        self.start = start
        self.end = end
        self.name = name
        self.length = length
        self.cars = cars
        self.lights = lights
        
    def __repr__(self):
        return f"Street {self.name} - (Start: {self.start}, End: {self.end}, Length: {self.length})."