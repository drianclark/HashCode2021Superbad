import input_parser
from intersection import Intersection
import random

def produce_schedule(intersections, streets, cars):
    # print(intersections)
    schedule = f"{len(intersections)}\n"
    for intersection in intersections.values():
        # first line with intersection ID
        schedule += f"{intersection.id}\n"
        # second line with number of incoming streets
        schedule += f"{len(intersection.incoming)}\n"
        # line for each incoming street
        for incomig_street in intersection.incoming.values():
            light_on_duration = random.randint(1,100) # TODO: how to represent how long it will have the light on??
            schedule += f"{incomig_street.name} {light_on_duration}\n" 
    return schedule

def createIntersections(num_intersections):
    """ all of our intersections - dict keyed by uid """
    intersections = {}
    for i in range(int(num_intersections)):
        uid = str(i)
        intersections[uid] = Intersection(uid)
    return intersections


# the main loop for the program
def main(input_file):
    ip = input_parser.InputParser(input_file)
    metadata = ip.getMetadata()
    duration, num_intersections, num_streets, num_cars, bonus = metadata
    print(f"File: {input_file}")
    print(f"Duration: {duration}; I: {num_intersections}; S: {num_streets}; C: {num_cars}; Bonus: {bonus}")

    
    intersections = createIntersections(num_intersections)

    # add streets to intersections
    streets = ip.getStreets()
    for street in streets:
        # connect to the egress intersection
        intersections[street.start].addOutgoingStreet(street)
        # print(f"Adding outgoing street {street} to intersection {intersections[street.start].id}")
        # connect to the ingress intersection
        intersections[street.end].addIncomingStreet(street)
        # print(f"Adding incoming street {street} to intersection {intersections[street.end].id}")
        # print(f"Intersection incoming: {intersections[street.start].incoming}")
        # print(f"Intersection outgoing: {intersections[street.end].outgoing}")
        # if street.start == 0:
        #     print(f"I: {intersections[street.start]}")

    #print(streets[0])
    cars = ip.getCars()
    #print(cars[0])
        
    # streetMap = {}
    
    # for street in streets:
    #     streetMap[street.name] = street
    # print(f"{streetMap}")
        
    # carMap = {}
    # for car in cars:
    #     carMap[car.id] = car
    # print(f"{carMap}")

    # for car, carObject in carMap.items():
    #     print(f"Car street: {carObject.street}")
    #     print(f"Street '{carObject.street}' cars: {streetMap[carObject.street].cars}")
    #     streetMap[carObject.street].cars.append(car)
    #     print(f"Street '{carObject.street}' cars: {streetMap[carObject.street].cars}")
    
    # for street in streets:
    #     print(street.name)
    #     print(street.cars)
    #     print()

    # produce the output file
    out_file = input_file.split(".")[0] + ".out"
    with open(out_file, 'w') as f:
        schedule = produce_schedule(intersections, streets, cars)
        print(f"Writing schedule to {out_file}.")
        f.write(schedule)

if __name__ == "__main__":
    input_files = ['d.txt'] #['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
    for input_file in input_files:
        main(input_file)