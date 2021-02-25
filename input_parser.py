# from . import Street

class InputParser:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def getMetadata(self):
        with open(self.input_file) as f:
            metadata = f.readline().rstrip("\n").split(" ")
            
        return metadata
            
    def getStreets(self):
        with open(self.input_file) as f:
            streetLines = f.readlines()[1:]
            for line in streetLines:
                lineContents = line.rstrip("\n").split(" ")
                
                try:
                    x = int(lineContents[1]) 
                except:
                    break
                
                start, end, name, length = lineContents
                print(start, end, name, length)
    
    def getPaths(self):
        with open(self.input_file) as f:
            streetLines = f.readlines()[1:]
            
            for line in streetLines:
                lineContents = line.rstrip("\n").split(" ")
                                
                if lineContents[1].isnumeric():
                    continue
                else:
                    car_id = lineContents[0]
                    car_path = lineContents[1:]
                    
                    print(car_id)
                    print(car_path)
                    print()

        
a = InputParser("a.txt")
a.getStreets()
a.getPaths()