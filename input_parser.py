import street
from car import Car
class InputParser:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def getMetadata(self):
        with open(self.input_file) as f:
            metadata = f.readline().rstrip("\n").split(" ")
            
        return metadata
            
    def getStreets(self):
        streets = []
        with open(self.input_file) as f:
            streetLines = f.readlines()[1:]
            for line in streetLines:
                lineContents = line.rstrip("\n").split(" ")
                
                try:
                    x = int(lineContents[1]) 
                except:
                    break
                
                start, end, name, length = lineContents
                streets.append(street.Street(name, length, start, end))
        return streets
    
    def getCars(self):
        cars = []
        with open(self.input_file) as f:
            streetLines = f.readlines()[1:]
            
            for line in streetLines:
                lineContents = line.rstrip("\n").split(" ")
                                
                if lineContents[1].isnumeric():
                    continue
                else:
                    car_id = lineContents[0]
                    car_path = lineContents[1:]
                    car_street = lineContents[1]
                    
                    carObject = Car(car_id, car_path, car_street)
                    cars.append(carObject)
                   
        return cars
