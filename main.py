import input_parser

def produce_schedule(intersections, streets, cars):
    schedule = f"{len(intersections)}\n"
    for intersection in intersections:
        # first line with intersection ID
        schedule += "{intersection.id}\n"
        # second line with number of incoming streets
        schedule += f"{len(intersection.incoming)}\n"
        # line for each incoming street
        for incomig_street in intersection.incomig:
            light_on_duration = 0 # TODO: how to represent how long it will have the light on??
            schedule += f"{incomig_street.name} {light_on_duration}" 
    return schedule

# the main loop for the program
def main(input_file):
    ip = input_parser.InputParser(input_file)
    metadata = ip.getMetadata()
    duration, num_intersections, num_streets, num_cars, bonus = metadata
    print(f"File: {input_file}")
    print(f"Duration: {duration}; I: {num_intersections}; S: {num_streets}; C: {num_cars}; Bonus: {bonus}")
    
    streets = ip.getStreets()
    #print(streets[0])
    cars = ip.getCars()
    #print(cars[0])
    intersections = []

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