class Street:
    def __init__(self, name, length, start, end, lights, cars=None):
        self.length = length
        self.start = start
        self.end = end
        self.name = name
        self.cars = cars
        self.lights = lights
        