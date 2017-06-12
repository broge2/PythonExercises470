def read_file_to_tuple(file_location):
    result = None
    with open(file_location) as file_h:
        result = [line.strip().lower() for line in file_h]
    return tuple(result)
    
file_loc = raw_input("File location: ")
name = raw_input("Who are you searching for: ").lower()

names_tuple = read_file_to_tuple(file_loc)
if name in names_tuple:
    print "Found"
else:
    print "Sorry, not found."
            