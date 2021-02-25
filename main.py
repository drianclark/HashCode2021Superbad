import input_parser
from intersection import Intersection

def produce_schedule(intersections, streets, cars):
    print(intersections)
    schedule = f"{len(intersections)}\n"
    for intersection in intersections.values():
        # first line with intersection ID
        schedule += "{intersection.id}\n"
        # second line with number of incoming streets
        schedule += f"{len(intersection.incoming)}\n"
        # line for each incoming street
        for incomig_street in intersection.incoming.values():
            light_on_duration = 0 # TODO: how to represent how long it will have the light on??
            schedule += f"{incomig_street.name} {light_on_duration}" 
    return schedule

def createIntersections(num_intersetions):
    """ all of our intersections - dict keyed by uid """
    intersections = {}
    for i in range(int(num_intersetions)):
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
        # connect to the ingress intersection
        intersections[street.end].addIncomingStreet(street)

    #print(streets[0])
    cars = ip.getCars()
    #print(cars[0])

    # produce the output file
    out_file = input_file.split(".")[0] + ".out"
    with open(out_file, 'w') as f:
        schedule = produce_schedule(intersections, streets, cars)
        print(f"Writing schedule to {out_file}.")
        f.write(schedule)


if __name__ == "__main__":
    input_files = ['a.txt'] #'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
    for input_file in input_files:
        main(input_file)