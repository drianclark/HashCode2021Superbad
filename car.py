class Car:
    def __init__(self, id, path, street):
        self.id = id
        self.path = path # modify path in place to remove visited intersections?
        self.street = street

    def __repr__(self):
        return f"Car {self.id} - Path: {self.path}"