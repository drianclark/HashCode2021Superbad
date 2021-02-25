class Intersection:
    def __init__(self, uid):
        """
        id : the unique idenity of this intersection
        on_light : name of street that is currently GREEN
        incoming : dict of connecting (incoming) Street objects keyed by name 
        outgoing : dict of outgoing Street objects keyed by name
        """
        self.id = uid
        self.incoming = {} 
        self.outgoing = {}
        self.on_light = None

    def go(self, street):
        """
        Takes a street object as input, set this street's traffic light to GREEN
        and all other lights connected to this intersection 
        """
        if street.name not in self.incoming:
            if street.name in self.outgoing:
                raise Exception(f"{street.name} is an outgoing street for this intersection")
            else:
                raise Exception(f"{street.name} is not connected to this intersection")
        else:
            # set all to red
            for street in self.incoming:
                street.light.setRed()
            
            # change only the light of the specified street to green
            self.incoming[street.name].light.setGreen()
            self.on_light = street.name


    def addIncomingStreet(self, street):
        if street.name in self.outgoing:
            raise Exception(f"{street.name} is already outgoing from this intersection")
        if street.name not in self.incoming:
            self.incoming[street.name] = street
        else:
            print("street is already incoming to this intersection")


    def addOutgoingStreet(self, street):
        if street.name in self.incoming:
            raise Exception(f"{street.name} is already incoming to this intersection")
        if street.name not in self.outgoing:
            self.incoming[street.name] = street
        else:
            print("street is already outgoing from this intersection")
