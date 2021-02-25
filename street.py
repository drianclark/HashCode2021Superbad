class Street:
    def __init__(self, name, length, start, end, cars=[], is_green=False):
        self.length = length
        self.start = start
        self.end = end
        self.name = name
        self.cars = cars
        self.is_green = False
        