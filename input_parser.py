from . import Street

class InputParser:
    def __init__(self, input_file):
        self.in = input_file
    
    def getMetadata(self):
        with open(self.in) as f:
            metadata = f.readline().rstrip("\n").split(" ")
            
        return metadata
            
    def getStreets(self):
        with open(self.in) as f:
            streetLines = f.readlines()[1:]
            for line in streetLines:
                lineContents = line.rstrip("\n").split(" ")
                
                try:
                    x = int(lineContents[1]) 
                except:
                    break
            
                streetObject = Street(lineContents[0], lineContents[1], lineContents[2], lineContents[3])
