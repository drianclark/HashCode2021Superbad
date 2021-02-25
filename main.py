import input_parser

# def summarise(streets, cars, paths):
#     print(f"Summary of the file:")
#     print(f"Streets: {len(streets)}.")
#     print(f"Cars: {len(cars)}.")
#     print(f"Paths: {len(paths)}.")

# the main loop for the program
def main(input_file):
    ip = input_parser.InputParser(input_file)
    metadata = ip.getMetadata()
    duration, num_intersections, num_streets, num_cars, bonus = metadata
    print(f"File: {input_file}")
    print(f"Duration: {duration}; I: {num_intersections}; S: {num_streets}; C: {num_cars}; Bonus: {bonus}")
    
    streets = ip.getStreets()
    print(streets[0])
    # cars = ip.getCars()
    cars = ip.getCars()
    print(cars[0])

    # summarise the input file
    # summarise(streets, cars, paths)

if __name__ == "__main__":
    input_files = ['a.txt'] #'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
    for input_file in input_files:
        main(input_file)